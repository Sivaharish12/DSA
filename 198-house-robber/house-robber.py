class Solution:
    def rob(self, nums: list[int]) -> int:
        memo={}
        def rec(ind):
            if ind in memo: return memo[ind]
            if ind>=len(nums): return 0
            pick=nums[ind]+rec(ind+2)
            skip=rec(ind+1)
            memo[ind]=max(pick,skip)
            return max(pick,skip)
        return rec(0)