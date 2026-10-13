class Solution:
    def minEatingSpeed(self, arr: List[int], h: int) -> int:
        l = 1
        r = max(arr)
        res = r
        while l<=r:
            mid = (l + r) // 2
            hours = 0
            for i in arr:
                hours += (i + mid-1)//mid
            if hours <= h:
                res = mid
                r = mid - 1
            
            else:
                l = mid +1
                
        return res