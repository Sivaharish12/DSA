class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo={}
        def rec(ind,nums,ans,count):
            if (ind,ans) in memo: return memo[(ind,ans)]
            if ind==len(nums):
                if ans==target: return 1
                return 0

            add=rec(ind+1,nums,ans+nums[ind],count)
            sub=rec(ind+1,nums,ans-nums[ind],count)
            memo[(ind,ans)]=add+sub
            return memo[(ind,ans)]
        return rec(0,nums,0,0)

        