class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        miss = n*(n+1)//2
        z = miss - sum(nums)
        return z