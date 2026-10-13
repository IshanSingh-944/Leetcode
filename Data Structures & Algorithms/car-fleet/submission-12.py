class Solution:
    def carFleet(self, t: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)
        dist = [(t - p)/s for (p,s) in pair]
        for i in dist:
            stack.append(i)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)