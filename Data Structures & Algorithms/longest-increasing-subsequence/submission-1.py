class Solution:
    def lengthOfLIS(self, nums: List[int]):
        max_len = 1
        lst = [nums[0]]
        for num in nums[1:]:
            if num > lst[-1]:
                lst.append(num)
                max_len+=1
            else:
                l , r = 0 , len(lst) - 1
                while l < r:
                    mid = (l + r)//2
                    if lst[mid] < num:
                        l = mid+1
                    else:
                        r = mid
                lst[l] = num
        return max_len
            

