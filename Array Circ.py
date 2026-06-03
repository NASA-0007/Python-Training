l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for i in range (0,len(l1)//4):
    temp=l1[i]
    a=l1[-(i+(len(l1)//2)+1)]
    l1[i]=a
    l1[-(i+(len(l1)//2)+1)]=temp
print(l1)