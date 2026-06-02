num = int(input())
count = 0
for j in range (2, int(num**0.5) + 1):
    if num % j == 0:
        count += 1
if count == 0 and num > 1:
    print("Prime")
else:
    print("Not Prime")