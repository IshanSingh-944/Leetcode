import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        heap = [(0,k)]
        dist = {}
        while heap:
            cost , curr = heapq.heappop(heap)
            if curr in dist:
                continue
            dist[curr] = cost
            for nei,w in graph[curr]:
                if nei not in dist:
                    heapq.heappush(heap,(w+cost,nei))
        return max(dist.values()) if len(dist)  ==n else  -1 
        