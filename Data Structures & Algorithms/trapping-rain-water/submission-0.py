class Solution:
    def trap(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        leftmax = arr[left]
        rightmax = arr[right]
        water = 0
        while left< right:
            if leftmax < rightmax:
                water += leftmax - arr[left]
                left+=1
                leftmax = max(leftmax,arr[left])
            else:
                water+= rightmax - arr[right]
                right -= 1
                rightmax = max(rightmax,arr[right])
        return water