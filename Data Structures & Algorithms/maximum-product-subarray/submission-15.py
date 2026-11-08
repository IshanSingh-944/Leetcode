class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = nums[0]
        mini = nums[0]
        max_prod = maxi

        for num in nums[1:]:
            temp = maxi
            maxi = max(num,num*maxi,num*mini)
            mini = min(mini*num,temp*num,num) 
            max_prod = max(max_prod,maxi)
            
            #print(temp,maxi,mini)
        return max_prod