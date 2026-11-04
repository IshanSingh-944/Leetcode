class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        a,b = 0, 0
        for i in range(len(nums)):
            curr = max(b,a+nums[i])
            a = b
            b = curr
        return curr

        
        