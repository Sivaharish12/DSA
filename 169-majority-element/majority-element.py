class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        h={}
        max=0
        count=0
        for i in nums:
            if i in h:
                h[i]+=1
                if h[i]>count: 
                    max=i
                    count=h[i]
            else: h[i]=1
        return max
        