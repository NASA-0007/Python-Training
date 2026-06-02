n=int(input("Enter number of elements: "))
l1=[]
for i in range (n):
    a=int(input("Enter element: "))
    l1.append(a)
l2=[]
l1.sort()
for i in l1:
    if i%2!=0:
        l2.append(i)
    else:
        l2.insert(0,i)
print("Sorted list is: ",l2)