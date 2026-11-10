import subprocess,csv,re
ROOT='/Users/aiden/dev/teams/ASM/Devfit/Devfit_'
OUT='/Users/aiden/dev/teams/ASM/last-dance/collect/data/'
dates=['2026-07-01','2026-07-15','2026-08-01','2026-08-15','2026-08-21','2026-09-01','2026-09-15','2026-10-01','2026-10-15','2026-11-01','2026-11-05']
CODE=('.ts','.tsx','.mjs','.mts','.js','.cjs','.css','.java','.sql','.py','.kt','.gradle')
def g(r,*a): return subprocess.run(['git','-C',ROOT+r,*a],capture_output=True,text=True).stdout
def sumcount(out):
  t=0;n=0
  for l in out.splitlines():
    t+=int(l.rsplit(':',1)[1]); n+=1
  return n,t
rows=[]
import datetime as dt
def mainsha(r,d):
  lim=dt.datetime.fromisoformat(d+'T00:00:00+09:00')
  best=None
  for l in open(f'/private/tmp/claude-501/-Users-aiden-dev-teams-ASM/44e5b55b-bef1-4a3a-8ba1-583a405dcd7e/scratchpad/runs_{r}.tsv'):
    f=l.rstrip('\n').split('\t')
    if f[2]=='push' and f[3]=='main':
      t=dt.datetime.fromisoformat(f[6].replace('Z','+00:00'))
      if t<lim and (best is None or t>best[0]): best=(t,f[9])
  if best: return best[1]
  return g(r,'rev-list','-1','--first-parent',f'--before={d}T00:00:00+09:00','origin/main').strip()
for r in 'FE','BE':
  for d in dates:
    sha=mainsha(r,d)
    if not sha:
      rows.append(dict(repo=r,snapshot_kst=d+' 00:00',sha='',files=0)); continue
    files=g(r,'ls-tree','-r','--name-only',sha).split('\n')
    code=[f for f in files if f.endswith(CODE) and 'package-lock' not in f]
    if r=='BE':
      tf=[f for f in code if f.startswith('src/test/') and f.endswith('.java')]
      tm=g(r,'grep','-c','-E',r'^[[:space:]]*@(Test|ParameterizedTest|RepeatedTest)([[:space:](]|$)',sha,'--','src/test')
      e2e=(0,0)
      mig=[f for f in files if re.match(r'src/main/resources/db/migration/V\d+__',f)]
      jm=[f for f in files if re.match(r'src/main/java/db/migration/V\d+__',f)]
      vs=[int(re.search(r'/V(\d+)__',f).group(1)) for f in mig+jm]
      migc=len(set(vs)); maxv=max(vs) if vs else 0
    else:
      tf=[f for f in code if re.search(r'\.(test|spec)\.(ts|tsx|mts|js)$',f) and not f.startswith('e2e/')]
      tm=g(r,'grep','-c','-E',r'^[[:space:]]*(it|test)(\.(each|only|skip|todo|concurrent))*[(`]',sha,'--',*[f for f in tf]) if tf else ''
      ef=[f for f in files if f.startswith('e2e/') and re.search(r'\.(spec|test)\.ts$',f)]
      e2e=(len(ef),sumcount(g(r,'grep','-c','-E',r'^[[:space:]]*test(\.[a-z]+)*\(',sha,'--','e2e'))[1] if ef else 0)
      migc=maxv=''
    tmn=sumcount(tm)[1] if tm else 0
    # LOC
    loc_main=loc_test=0
    lc=g(r,'grep','-c','-I','',sha,'--',*[f'*{e}' for e in CODE])
    for l in lc.splitlines():
      path=l.split(':',1)[1].rsplit(':',1)[0]; c=int(l.rsplit(':',1)[1])
      if 'package-lock' in path: continue
      if path in set(tf) or path.startswith('src/test/') or path.startswith('e2e/'): loc_test+=c
      else: loc_main+=c
    rows.append(dict(repo=r,snapshot_kst=d+' 00:00',sha=sha[:9],files=len(files),code_files=len(code),loc_code_nontest=loc_main,loc_test=loc_test,test_files=len(tf),test_methods=tmn,e2e_files=e2e[0],e2e_tests=e2e[1],flyway_versions=migc,flyway_max_V=maxv))
    print(rows[-1])
with open(OUT+'growth_tests_loc_flyway.csv','w') as f:
  keys=list(rows[-1]); w=csv.DictWriter(f,fieldnames=keys,restval='');w.writeheader();w.writerows(rows)
