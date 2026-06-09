l1=[1,2,3,4,5,6,7]
rot=int(input("Enter number of rotations: "))
k=0
for i in range (-((len(l1)//2)+1),0):
    temp=l1[i]
    a=l1[-(i+((len(l1)//2)+1))]
    l1.pop(i)
    l1.insert(k,temp)
    k += 1
    if k==rot:
        break

# temp=l1[-1]
# # a=l1[-(-1+((len(l1)//2)+1))]
# l1.pop(-1)
# # l1[-(-1+((len(l1)//2)+1))]=temp
# l1.insert(k,temp)
print(l1)