class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        sum = 0
        for num in nums:
            if sum < 0:
                sum = 0
            sum += num
            curr = max(sum,curr)
        return curr