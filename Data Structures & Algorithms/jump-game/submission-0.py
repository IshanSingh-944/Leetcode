class Solution:
    def canJump(self, nums: List[int]):
        n = len(nums) - 1
        goal = n
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
