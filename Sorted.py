l1=[2,3,4,7,8,9]
l2=[1,5,6]
j=0
i=0
while j<len(l2) and i<len(l1):
    if l1[i]>l2[j]:
        l1.insert(i,l2[j])
        j += 1
    i += 1

while j<len(l2):
    l1.append(l2[j])
    j += 1

print(l1)