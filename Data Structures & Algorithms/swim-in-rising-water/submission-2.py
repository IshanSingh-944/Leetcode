class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [[grid[0][0], 0, 0]]
        n = len(grid)
        ans = 0
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        seen = set()
        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return cost
            for dr, dc in dir:
                nr = r + dr
                nc = c + dc
                if nr < 0 or nc < 0 or nr == n or nc == n or (nr,nc) in seen:
                    continue
                seen.add((nr,nc))
                heapq.heappush(heap,(max(cost,grid[nr][nc]),nr,nc))