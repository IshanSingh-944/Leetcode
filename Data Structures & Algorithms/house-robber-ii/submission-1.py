class Solution:
    def x(self,arr):
        a,b = 0,0
        for i in range(len(arr)):
            curr = max(arr[i]+a,b)
            a = b
            b = curr
        return curr

    def rob(self, nums: List[int]):
        if len(nums) == 1:
            return nums[0]
        return max(self.x(nums[1:]),self.x(nums[:-1]))
       