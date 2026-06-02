n=int(input("Enter a number: "))
sums=0
exp=len(str(n))
exps=1
a=n
rev=0
while a:
    rem=a%10
    rev=rev*10+rem
    a=a//10
while rev:
    rem=rev%10
    sums+=rem**exps
    rev=rev//10
    exps+=1
print("The number is: ",sums)