digits=[9,9,9]
# a=''.join(map(str, digits))
# b=int(a)
# b+=1
# digits=[int(x) for x in str(b)]
# print(digits)
for i in range(len(digits)-1,-1,-1):
    if digits[i]<9:
        digits[i]+=1
        break
    else:
        digits[i]=0
if digits[0]==0:
    digits.insert(0,1)
print(digits)