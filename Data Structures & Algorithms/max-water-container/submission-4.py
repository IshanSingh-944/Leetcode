class Solution:
    def maxArea(self, arr: List[int]) -> int:
        
        water = 0
        left = 0
        right = len(arr)-1
        while left < right:
            h = min(arr[left],arr[right])
            hold = (h*(right-left))
            if hold > water:
                water = hold 
            if arr[left]< arr[right]:
                left+=1
            else:
                right -= 1
        return water