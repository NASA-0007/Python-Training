def countdown(k,t=1,r=1):
    print(t,end=" ")
    if t!=k and r:
        return countdown(k,t+1)
    elif t>1:
        return countdown(k,t-1,0)
countdown(int(input("Enter Number: ")))