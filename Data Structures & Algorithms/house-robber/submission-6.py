class Solution:
    def rob(self, arr: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # if len(nums) == 2:
        #     return max(nums[0],nums[1])
        # a,b = 0, 0
        # for i in range(2,len(nums)):
        #     curr = max(b,a+nums[i])
        #     a = b
        #     b = curr
        # return a

        
        a,b = 0,0
        for i in range(len(arr)):
            curr = max(arr[i]+a,b)
            a = b
            b = curr
        return curr