# a=list(map(int, input().split()))
# b=int(input())
# m=0
# s=0
# for i in range(len(a)-b+1):
#     for j in range(i, i+b):
#         s=s+a[j]
#     if s>m:
#         m=s
#     s=0
# print("Max is :", m)



a = list(map(int, input().split()))
b = int(input())
w = sum(a[:b])
m = w
for i in range(b, len(a)):
    w = w - a[i - b] + a[i]
    print(w)
    if w > m:
        m = w
print("Max is :", m)