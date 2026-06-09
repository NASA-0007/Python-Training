chars = "aaabbbcccbbbssstttniagga;;s'a'"
new=""
count=1
now=chars[0]
for i in range (1,len(chars)):
    if now==chars[i]:
        count+=1
    else:
        new+=now+str(count)
        now=chars[i]
        count=1
new+=now+str(count)

print (new)
