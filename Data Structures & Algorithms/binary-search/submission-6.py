class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left = 0 
        right = len(arr)-1
        while left <= right:
            mid = (right + left)//2
            if arr[mid] == target:
                return mid
            if target < arr[mid]:
                right = mid - 1
            else:
                left = mid+1
        return -1
