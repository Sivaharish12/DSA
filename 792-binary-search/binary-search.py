class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def rec(start,end):
            if(end-start)<1: return -1
            mid=(start+end)//2
            if nums[mid]==target: return mid
            if(nums[mid]<target): return rec(mid+1,end)
            if(nums[mid]>target): return rec(start, mid)
        return rec(0,len(nums))
        