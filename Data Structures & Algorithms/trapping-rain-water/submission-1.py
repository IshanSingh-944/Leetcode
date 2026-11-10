class Solution:
    def trap(self, arr: List[int]) -> int:
        water = 0
        left,right = 0, len(arr) - 1
        leftmax,rightmax = arr[left],arr[right]
        while left < right:
            if leftmax < rightmax:
                water += leftmax - arr[left]
                left += 1
                leftmax = max(leftmax,arr[left])
            else:
                water += rightmax - arr[right]
                right -= 1
                rightmax = max(rightmax,arr[right])
        return water