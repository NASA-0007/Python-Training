def fun(n):
    if n==0:
        return 200
    t=fun(n-1)
    print(n,end=" ")
    return t

n=5
print(fun(n))