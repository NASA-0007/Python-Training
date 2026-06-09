def countdown(k):
    print(k,end=" ")
    if k>1:
        return countdown(k-1)
    
countdown(int(input("Enter Number: ")))