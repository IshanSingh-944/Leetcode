class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        ans = nums[0]
        for i in nums[1:]:
            temp = max(i,maxi*i,mini*i)
            mini = min(i,maxi*i,mini*i)
            maxi = temp 
            ans = max(ans,maxi)
        return ans