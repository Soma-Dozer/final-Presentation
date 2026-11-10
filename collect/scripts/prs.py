import json,csv,datetime as dt,collections,re
KST=dt.timezone(dt.timedelta(hours=9)); B=dt.datetime(2026,8,21,tzinfo=KST)
p=lambda s: dt.datetime.fromisoformat(s.replace('Z','+00:00')).astimezone(KST)
OUT='/Users/aiden/dev/teams/ASM/last-dance/collect/data/'
def q(xs,f):
  xs=sorted(xs); k=(len(xs)-1)*f; i=int(k); return xs[i]+(xs[min(i+1,len(xs)-1)]-xs[i])*(k-i)
rows=[]
for r in 'FE','BE':
  for x in json.load(open(f'pr_{r}.json')):
    rv=x['reviews']; cm=x['comments']
    rev_humans={y['author']['login'] for y in rv if y.get('author')}
    pa=x['author']['login'] if x.get('author') else ''
    cm_bots=[y for y in cm if y.get('author') and ('bot' in y['author']['login'].lower() or y['author']['login'] in('coderabbitai','github-actions'))]
    rows.append(dict(repo=r,number=x['number'],title=x['title'],author=pa,base=x['baseRefName'],head=x['headRefName'],state=x['state'],created_kst=p(x['createdAt']).isoformat(),merged_kst=p(x['mergedAt']).isoformat() if x['mergedAt'] else '',
      ttm_h=round((p(x['mergedAt'])-p(x['createdAt'])).total_seconds()/3600,2) if x['mergedAt'] else '',
      reviews=len(rv),reviewers=';'.join(sorted(rev_humans)),review_by_other=int(bool(rev_humans-{pa})),approved=int(any(y['state']=='APPROVED' for y in rv)),
      comments=len(cm),comment_authors=';'.join(sorted({y['author']['login'] for y in cm if y.get('author')})),bot_comments=len(cm_bots),
      additions=x['additions'],deletions=x['deletions'],files=x['changedFiles']))
with open(OUT+'prs_all.csv','w') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
m=[x for x in rows if x['merged_kst']]
print('merged',len(m), collections.Counter((x['repo'],x['base']) for x in m))
print('authors',collections.Counter(x['author'] for x in m))
print('all comment authors',collections.Counter(a for x in rows for a in x['comment_authors'].split(';') if a))
print('all reviewers',collections.Counter(a for x in rows for a in x['reviewers'].split(';') if a))
for lab,sel in (('all',lambda x:True),('to_prod',lambda x:x['base']=='prod'),('to_staging',lambda x:x['base']=='staging'),('to_main',lambda x:x['base']=='main'),('pre',lambda x:p(x['merged_kst'])<B),('post',lambda x:p(x['merged_kst'])>=B)):
  s=[x for x in m if sel(x)]
  if not s: continue
  t=[x['ttm_h'] for x in s]
  print(lab,len(s),'review_any %.1f%%'%(100*sum(x['reviews']>0 for x in s)/len(s)),'review_by_other %.1f%%'%(100*sum(x['review_by_other'] for x in s)/len(s)),'approved %.1f%%'%(100*sum(x['approved'] for x in s)/len(s)),'comment_any %.1f%%'%(100*sum(x['comments']>0 for x in s)/len(s)),'ttm median h %.2f p90 %.1f'%(q(t,.5),q(t,.9)))
# hotfix
hf=[x for x in m if re.search(r'hotfix|fix/|긴급|rollback|롤백|revert',x['head']+' '+x['title'],re.I) and x['base'] in('staging','prod')]
print('fix PRs into staging/prod',len(hf),collections.Counter((('pre' if p(x['merged_kst'])<B else 'post'),x['base']) for x in hf))
hh=[x for x in m if re.search(r'hotfix',x['head']+' '+x['title'],re.I)]
print('hotfix-named', len(hh), [(x['repo'],x['number'],x['base'],x['title'][:50]) for x in hh])
# direct to prod not from staging
print('prod base non-staging head', [(x['repo'],x['number'],x['head'],x['merged_kst'][:10]) for x in m if x['base']=='prod' and x['head']!='staging'])
