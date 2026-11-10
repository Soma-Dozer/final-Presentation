import numpy as np
# digitized cumulative members (admin growth chart, 365d, 11-04 12:32), +-1
pts = {"08-07":7,"08-16":9,"08-23":11,"08-30":15,"09-06":23,"09-13":28,"09-20":35,"09-27":40,
       "10-04":58,"10-11":63,"10-18":70,"10-25":71,"11-01":82,"11-04":83}
keys=list(pts)
wk_start=["08-24","08-31","09-07","09-14","09-21","09-28","10-05","10-12","10-19","10-26"]
adds=[pts[keys[i+1]]-pts[keys[i]] for i in range(2,12)]
gcost=[43756,10963,16,487,84031,185330,415553,224413,27541,113605]
gclk=[251,73,0,2,88,882,424,117,43,73]
gconv=[0,0,0,0,2,3,12,5,1,3]
for w,a,c in zip(wk_start,adds,gcost): print(w,a,c)
print("pearson adds~google cost", np.corrcoef(adds,gcost)[0,1])
print("pearson adds~google clicks", np.corrcoef(adds,gclk)[0,1])
print("pearson adds~google conv", np.corrcoef(adds,gconv)[0,1])
# run rates
print("8wk 9/6->11/1:",(82-23)/8, " 4wk 10/4->11/1:",(82-58)/4)
# monthly
mon={"8월":(533,15-7,46),"9월":(10991,55-15,9879),"10월":(12077,81-55,10101),"11월1~4":(163,83-81,None)}
for m,(s,g,ig) in mon.items(): print(m,s,g,round(g/s*1000,2),"per1k")
nonig=(10991-9879)+(12077-10101); ig=9879+10101; sg=40+26
for r in (0.012,0.015):
    exp=nonig*r; igs=sg-exp; print("rate",r,"nonIG exp",round(exp,1),"IG signups",round(igs,1),"IGconv%",round(igs/ig*100,3),"Meta CPS",round(2338208/igs))
spend=2338208+1136972
print("blended per signup",spend/83, spend/79)
