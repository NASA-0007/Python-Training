def countdown(k,o=None,r=0):
    if o==None:
        o=k
    print(k,end=" ")
    if k>1 and not r:
        return countdown(k-1,o)
    elif k!=o:
        return countdown(k+1,o,1)
countdown(int(input("Enter Number: ")))