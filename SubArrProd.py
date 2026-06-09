class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        length=0
        r,l,s,m=0,0,1,0
        while r<len(nums):
            s*=nums[r]
            while s>=k:
                s=s//nums[l]
                l+=1
            length+=r-l+1
            r+=1
        print(length)
        return length