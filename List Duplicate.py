n=int(input("Enter number of elements: "))
l1=[]
for i in range (n):
    a=int(input("Enter element: "))
    l1.append(a)
count=0
l2=[]
for i in l1:
    # for j in range (i+1,n-1):
    #     if l1[i]==l1[j]:
    #         count+=1
    #         break
    # if count==1:
    #     l1.pop(j)
    if i not in l2:
        l2.append(i)
print("Unique elements are: ",l2)