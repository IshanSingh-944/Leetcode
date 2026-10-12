import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x,y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        heap = [(0,0)]
        total = 0
        seen = set()
        n = len(points)
        while len(seen)<n:
            dist,curr = heapq.heappop(heap)
            if curr in seen:
                continue
            seen.add(curr)
            total += dist
            for next in range(n):
                if next not in seen:
                    dis = distance(points[curr],points[next])
                    heapq.heappush(heap,(dis,next))
        return total
