n=int(input("Enter a number: "))
sums=0
exp=len(str(n))
exps=1
while n:
    rem=n%10
    sums+=rem**exps
    n=n//10
    exps+=1
print("The number is: ",sums)