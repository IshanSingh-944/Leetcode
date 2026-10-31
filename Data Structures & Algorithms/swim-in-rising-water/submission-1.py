class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [[grid[0][0],0,0]]
        seen = set()
        seen.add((0,0))
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        while heap:
            t,r,c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return t
            for dr , dc in dir:
                nr = dr + r 
                nc = dc + c
                if nr < 0 or nc < 0 or (nr,nc) in seen or nr == n or nc == n:
                    continue
                seen.add((nr,nc))
                heapq.heappush(heap,(max(grid[nr][nc],t),nr,nc))

