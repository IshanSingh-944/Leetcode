class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        leng = 0
        nums = set(nums)
        print(nums)
        for i in nums:
            if i-1 not in nums:
                start = i
                ans = 1
                while start+1 in nums:
                    start = start+1
                    ans += 1
                if ans>leng:
                    leng = ans
                
        return leng