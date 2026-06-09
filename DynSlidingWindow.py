r,l,s,m=0,0,0,0
while r<len(nums):
    s+=nums[r]
    while s>k:
        s-=nums[l]
        l+=1
    length=r-l+1
    m=max(m, length)
    r+=1
print(m)