a=int(input("Enter a number: "))
rev=0
while a:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print("Reverse of the number is: ",rev)