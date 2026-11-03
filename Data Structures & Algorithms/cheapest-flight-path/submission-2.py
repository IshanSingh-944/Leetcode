import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        heap = [(0,src,0)]
        dist = {}
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        while heap:
            cost , node, edges = heapq.heappop(heap)
            
            if edges > k+1:
                continue
            if node == dst:
                return cost
            if (node,edges) in dist and dist[(node,edges)]<=cost:
                continue
            dist[(node,edges)] = cost
            for nei,price in graph[node]:
                heapq.heappush(heap,(cost+price,nei,edges+1))
        return -1