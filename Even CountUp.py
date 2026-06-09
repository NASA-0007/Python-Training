def countdown(k,t=2):
    if k%2!=0:
        return
    print(t,end=" ")
    if t!=k:
        return countdown(k,t+2)
    
countdown(int(input("Enter Number: ")))