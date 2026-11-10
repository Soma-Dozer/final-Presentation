import csv,datetime as dt,collections
KST=dt.timezone(dt.timedelta(hours=9)); B=dt.datetime(2026,8,21,tzinfo=KST)
p=lambda s: dt.datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(KST)
OUT='/Users/aiden/dev/teams/ASM/last-dance/collect/data/'
rows=[]
for r,id,ev,br,cr,j in csv.reader(open('failed_jobs.tsv'),delimiter='\t'):
  jobs=set(x.split(' (')[0] for x in j.split(';') if x)
  if any(x.startswith('deploy') for x in jobs): cat='deploy_job_failed'
  elif 'verify-production-promotion' in jobs: cat='blocked_promotion_gate'
  elif 'block-analysis-on-production' in jobs and not ({'test','speech-local-test'}&jobs): cat='blocked_analysis_leak_gate'
  elif {'test','speech-local-test'}&jobs: cat='blocked_tests'
  else: cat='other'
  br2=br if br in('main','staging','prod') else 'feature'
  rows.append(dict(repo=r,run_id=id,event=ev,branch=br,branch_group=br2,created_kst=p(cr).isoformat(),period='pre' if p(cr)<B else 'post',failed_jobs=';'.join(sorted(jobs)),category=cat))
with open(OUT+'ci_failed_runs_by_job.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
c=collections.Counter((x['branch_group'],x['category']) for x in rows); 
for k,v in sorted(c.items()): print(k,v)
print(collections.Counter((x['period'],x['category']) for x in rows))
print(collections.Counter((x['repo'],x['category']) for x in rows))
