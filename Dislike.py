n=int(input())
l1=[]
l2=[]
for i in range(0,n):
    a=int(input())
    l1.append(a)
count=0
i=1
while count<=1000:
    if i %10 != 3 and i %3 != 0:
        l2.append(i)
        count+=1
    i+=1
for i in l1:
    print(l2[i-1])
