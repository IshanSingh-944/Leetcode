class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        res = [0]*len(arr)
        for idx , temp in enumerate(arr):
            while stack and arr[stack[-1]] < temp:
                curr = stack.pop()
                res[curr] = idx - curr
            stack.append(idx)
        return res
