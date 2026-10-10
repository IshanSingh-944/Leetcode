class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        res = 0
        nums = set(nums)
        if len(nums) == 1:
            return 1

        for i in nums:
            if i-1 not in nums:
                start = i
                res = 1
                while start+1 in nums:
                    start = start+1
                    res+=1
                if res>length:
                    length = res
        return length
            

            
            