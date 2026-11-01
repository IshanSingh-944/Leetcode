class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x,y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        heap = [(0,0)]
        seen = set()
        n = len(points)
        total = 0
        while len(seen) < n:
            cost, point = heapq.heappop(heap)
            if point not in seen:
                seen.add(point)
                total += cost
            else: 
                continue
            
            
            for next in range(n):
                if next not in seen:
                    
                    dis = dist(points[point],points[next])
                    heapq.heappush(heap,(dis,next))
        return total

