def countdown(k,t=1):
    print(t,end=" ")
    if t!=k:
        return countdown(k,t+1)
    
countdown(int(input("Enter Number: ")))