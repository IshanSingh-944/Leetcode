class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-s for s in stones]
        heapq.heapify(s)
        while len(s) > 1:
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            if b>a:
                heapq.heappush(s,a-b)
        s.append(0)
        return abs(s[0])if s else  0
