class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr = sorted(arr)
        for i in range(len(arr)):
            left = i+1
            right = len(arr) - 1
            if  i>0 and arr[i-1] == arr[i]:
                continue
            while left < right :
                target = arr[i]+arr[left]+arr[right]
                if target == 0:
                    ans.append([arr[i],arr[left],arr[right]])
                    while left<right and arr[left] == arr[left+1]:
                        left+=1
                    while left<right and arr[right] == arr[right-1]: 
                        right -= 1

                    left += 1
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    right -=1 
        return ans

