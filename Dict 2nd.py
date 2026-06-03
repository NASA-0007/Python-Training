l1=[1,2,3,4,2,2,4,2,4,6,3,35,2,12,5]
d={}
for i in l1:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(len(d))
d.pop(max(d))
print(max(d.keys()))