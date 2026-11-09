class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = prev1 = 0
        for i in range(len(nums)):
            curr = max(nums[i]+prev1,prev)
            prev1 = prev
            prev = curr
        return curr 