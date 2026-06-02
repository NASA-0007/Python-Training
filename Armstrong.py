n=int(input("Enter a number: "))
temp=n
sums=0
while n:
    rem=n%10
    sums+=rem**len(str(temp))
    n=n//10
if sums==temp:
    print("Armstrong")
else:
    print("Not Armstrong")