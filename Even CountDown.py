def countdown(k):
    if k%2!=0:
        return
    print(k,end=" ")
    if k>2:
        return countdown(k-2)
    
countdown(int(input("Enter Number: ")))