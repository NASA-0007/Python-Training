l1=[1, 2, 6,6,6,3, 4, 5,5,5]
m = 0
last = 0
for i in l1:
    if i > m:
        last = m
        m = i
    elif m>i and i>last:
        last = i
print(last)
