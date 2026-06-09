def countsteps(k,c=0):
    if k==1:
        return c
    elif k%2==0:
        c=c+1
        return countsteps(k/2,c)
    elif k%4==3:
        c=c+1
        return countsteps(k+1,c)
    else:
        c=c+1
        return countsteps(k-1,c)

print(countsteps(int(input())))