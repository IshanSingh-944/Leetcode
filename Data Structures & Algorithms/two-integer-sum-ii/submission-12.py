class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        for idx,num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp]+1,idx+1]
            seen[num] = idx
         
