import subprocess,csv,datetime as dt,collections
KST=dt.timezone(dt.timedelta(hours=9)); B=dt.datetime(2026,8,21,tzinfo=KST)
ROOT='/Users/aiden/dev/teams/ASM/Devfit/Devfit_'; OUT='/Users/aiden/dev/teams/ASM/last-dance/collect/data/'
CODE=('.ts','.tsx','.mjs','.mts','.js','.cjs','.css','.java','.sql','.py','.kt','.gradle')
rows=[];churn=collections.defaultdict(lambda:[0,0,0])
for r in 'FE','BE':
  out=subprocess.run(['git','-C',ROOT+r,'log','--remotes=origin','--format=%H\t%aI\t%an\t%P','--numstat'],capture_output=True,text=True).stdout
  cur=None
  for l in out.split('\n'):
    if '\t' in l and len(l.split('\t')[0])==40:
      h,ai,an,par=l.split('\t'); t=dt.datetime.fromisoformat(ai).astimezone(KST)
      cur=dict(repo=r,sha=h[:9],author=an,author_kst=t.isoformat(),date=t.date().isoformat(),hour=t.hour,weekday=t.strftime('%a'),is_merge=int(len(par.split())>1),period='pre' if t<B else 'post',add=0,dele=0)
      rows.append(cur)
    elif l and cur and l[0] in '0123456789-':
      a,d,f=l.split('\t',2)
      if a=='-' or not f.endswith(CODE) or 'package-lock' in f: continue
      cur['add']+=int(a);cur['dele']+=int(d)
print('total',len(rows),'merges',sum(x['is_merge'] for x in rows))
with open(OUT+'commits_remote_all.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
nm=[x for x in rows if not x['is_merge']]
print('non-merge',len(nm))
# heatmap
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
H=collections.Counter((x['weekday'],x['hour']) for x in nm)
with open(OUT+'commit_heatmap_weekday_hour_kst.csv','w') as f:
  w=csv.writer(f);w.writerow(['weekday']+[f'h{h:02d}' for h in range(24)]+['total'])
  for d in days: w.writerow([d]+[H[(d,h)] for h in range(24)]+[sum(H[(d,h)] for h in range(24))])
def share(sel,pred): s=[x for x in nm if sel(x)]; return len(s), round(100*sum(pred(x) for x in s)/len(s),1)
late=lambda x: x['hour']>=22 or x['hour']<6
night=lambda x: 0<=x['hour']<6
wkend=lambda x: x['weekday'] in('Sat','Sun')
for lab,sel in (('all',lambda x:True),('pre',lambda x:x['period']=='pre'),('post',lambda x:x['period']=='post'),('FE',lambda x:x['repo']=='FE'),('BE',lambda x:x['repo']=='BE')):
  print(lab,'n,late22-06%',share(sel,late),'00-06%',share(sel,night)[1],'weekend%',share(sel,wkend)[1])
print('by hour',[sum(H[(d,h)] for d in days) for h in range(24)])
print('by weekday',[(d,sum(H[(d,h)] for h in range(24))) for d in days])
ad=sorted({x['date'] for x in nm}); print('active days',len(ad),'of',(dt.date(2026,11,4)-dt.date(2026,6,29)).days+1)
for lab,pr in (('pre','pre'),('post','post')):
  s={x['date'] for x in nm if x['period']==pr}; print(lab,'active days',len(s))
# longest streak
ds=[dt.date.fromisoformat(d) for d in ad]; best=cur_=1
for a,b in zip(ds,ds[1:]):
  cur_=cur_+1 if (b-a).days==1 else 1; best=max(best,cur_)
print('longest streak',best)
# monthly churn
M=collections.defaultdict(lambda:[0,0,0])
for x in nm:
  k=(x['repo'],x['date'][:7]); M[k][0]+=1; M[k][1]+=x['add']; M[k][2]+=x['dele']
with open(OUT+'monthly_commits_churn.csv','w') as f:
  w=csv.writer(f);w.writerow(['repo','month','nonmerge_commits','code_lines_added','code_lines_deleted'])
  for k in sorted(M): w.writerow([*k,*M[k]]); print(k,M[k])
