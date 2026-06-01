n,m,a,b=map(int, input().split())

if ((n//m)*b < n*a):
    print((n//m)*b + min((n%m)*a, b))
else:
    print(n*a)
