n=int(input())
a=list(map(int,input().split()))
police=0
crime=0
for i in a:
    if i==-1 and police>0:
        police-=1
    elif i>=1:
        police+=i
    else:
        crime+=1
print(crime)