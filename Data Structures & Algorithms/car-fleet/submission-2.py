class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = list(zip(position, speed))
        pair.sort(reverse=True)
        dist = [(target - p) / s for p, s in pair]
        for i in dist:
            stack.append(i)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
