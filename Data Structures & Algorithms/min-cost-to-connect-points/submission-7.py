class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x,y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        heap = [(0,0)]
        ans = 0
        seen = set()
        
        while len(seen) < len(points):
            cost , p = heapq.heappop(heap)
            if p not in seen:
                ans += cost
                seen.add(p)
            else:
                continue
            for rest in  range(len(points)):
                if rest not in seen:
                    dis = dist(points[p],points[rest])
                    heapq.heappush(heap,(dis,rest))
        return ans

