import csv, json, subprocess, statistics as st, datetime as dt, collections, sys
KST=dt.timezone(dt.timedelta(hours=9)); B=dt.datetime(2026,8,21,tzinfo=KST)
OUT='/Users/aiden/dev/teams/ASM/last-dance/collect/data/'
ROOT='/Users/aiden/dev/teams/ASM/Devfit/'
S=sys.argv[1]
def p(s): return dt.datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(KST)
def q(xs,f):
  xs=sorted(xs); 
  if not xs: return None
  k=(len(xs)-1)*f; i=int(k); return xs[i]+(xs[min(i+1,len(xs)-1)]-xs[i])*(k-i)
runs=[]
for r in 'FE','BE':
  for row in csv.reader(open(f'{S}/runs_{r}.tsv'),delimiter='\t'):
    id,name,ev,br,stt,con,cr,up,rs,sha,att=row
    runs.append(dict(repo=r,id=id,name=name,event=ev,branch=br,conclusion=con,created=p(cr),updated=p(up),started=p(rs),sha=sha,attempt=att))
cicd=[x for x in runs if 'CI/CD' in x['name'] or x['name'] in('Frontend CI','Backend CI','.github/workflows/ci.yml')]
prod=[x for x in cicd if x['branch']=='prod' and x['event'] in('push','workflow_dispatch') and x['conclusion'] in('success','failure')]
prod.sort(key=lambda x:x['created'])
# weekly deploys
wk=collections.Counter(); wkf=collections.Counter()
for x in prod:
  y,w,_=x['created'].isocalendar(); key=f'{y}-W{w:02d}'
  (wk if x['conclusion']=='success' else wkf)[(key,x['repo'])]+=1
weeks=sorted({k for k,_ in list(wk)+list(wkf)})
with open(OUT+'dora_prod_deploys_weekly.csv','w') as f:
  w=csv.writer(f); w.writerow(['iso_week_kst','week_start_kst','FE_success','BE_success','total_success','FE_failed','BE_failed'])
  for k in weeks:
    y,n=k.split('-W'); ws=dt.date.fromisocalendar(int(y),int(n),1)
    w.writerow([k,ws,wk[(k,'FE')],wk[(k,'BE')],wk[(k,'FE')]+wk[(k,'BE')],wkf[(k,'FE')],wkf[(k,'BE')]])
def per_week(pre):
  xs=[x for x in prod if x['conclusion']=='success' and ((x['created']<B)==pre)]
  if not xs: return 0,0,0
  start=xs[0]['created'] if pre else B; end=B if pre else dt.datetime(2026,11,4,tzinfo=KST)
  days=(end-start).total_seconds()/86400
  return len(xs),round(days,1),round(len(xs)/days*7,1)
print('deploys pre',per_week(True),'post',per_week(False))
# weekly totals list
tot={k:wk[(k,'FE')]+wk[(k,'BE')] for k in weeks}
print('weekly totals',tot)
# change failure / MTTR
rows=[]
for r in 'FE','BE':
  xs=[x for x in prod if x['repo']==r]
  for i,x in enumerate(xs):
    if x['conclusion']=='failure':
      nxt=next((y for y in xs[i+1:] if y['conclusion']=='success'),None)
      # skip if previous also failure (count incident once from first failure)
      first = i==0 or xs[i-1]['conclusion']=='success'
      rows.append(dict(repo=r,run_id=x['id'],failed_at=x['created'].isoformat(),sha=x['sha'][:7],first_in_streak=first,next_success_at=nxt['updated'].isoformat() if nxt else '',recovery_min=round((nxt['updated']-x['created']).total_seconds()/60,1) if nxt else ''))
with open(OUT+'dora_prod_failures_mttr.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for lab,pre in (('pre',True),('post',False)):
  a=[x for x in prod if (x['created']<B)==pre]; fl=[x for x in a if x['conclusion']=='failure']
  inc=[r for r in rows if r['first_in_streak'] and (p(r['failed_at'])<B)==pre and r['recovery_min']!='']
  rec=[r['recovery_min'] for r in inc]
  print(lab,'prod attempts',len(a),'failed',len(fl),'rate',round(len(fl)/len(a)*100,1) if a else None,'incidents',len(inc),'MTTR median min',q(rec,.5),'p90',q(rec,.9))
# deploy duration (success prod)
for lab,pre in (('pre',True),('post',False)):
  for r in 'FE','BE':
    d=[(x['updated']-x['started']).total_seconds()/60 for x in prod if x['repo']==r and x['conclusion']=='success' and (x['created']<B)==pre and x['attempt']=='1']
    print('dur',lab,r,len(d),round(q(d,.5),1) if d else None,round(q(d,.9),1) if d else None)
# lead time
lt=[]
for r in 'FE','BE':
  g=lambda *a: subprocess.run(['git','-C',ROOT+'Devfit_'+r,*a],capture_output=True,text=True).stdout
  fp=g('log','--first-parent','--reverse','--format=%H %cI','origin/prod').split('\n')
  fp=[l.split() for l in fp if l]
  prev=None
  START=dt.datetime(2026,8,3,tzinfo=KST)
  for h,ci in fp:
    if p(ci)<START:
      prev=h; continue
    rng=[h] if prev is None else [f'{prev}..{h}']
    out=g('log','--no-merges','--format=%H\t%aI\t%an\t%s',*rng)
    for l in out.split('\n'):
      if not l: continue
      c,ai,an,s=l.split('\t',3)
      lt.append(dict(repo=r,commit=c[:9],author_at=p(ai).isoformat(),prod_at=p(ci).isoformat(),prod_commit=h[:9],lead_h=round((p(ci)-p(ai)).total_seconds()/3600,2),subject=s[:80]))
    prev=h
with open(OUT+'dora_lead_time_commits.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=list(lt[0])); w.writeheader(); w.writerows(lt)
for lab,pre in (('pre',True),('post',False),('all',None)):
  for r in ('FE','BE','ALL'):
    xs=[x['lead_h'] for x in lt if (r=='ALL' or x['repo']==r) and (pre is None or (p(x['prod_at'])<B)==pre)]
    print('lead',lab,r,len(xs),'median h',round(q(xs,.5),1),'p90 h',round(q(xs,.9),1))
