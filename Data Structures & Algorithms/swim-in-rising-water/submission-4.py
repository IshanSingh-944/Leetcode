class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col =  len(grid[0])
        heap = [(grid[0][0],0,0)]
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()
        while heap:
            t,r,c = heapq.heappop(heap)
            if r == row-1 and c == col - 1:
                return t
            for dr,dc in dir:
                nr = dr + r
                nc = dc + c
                if nr<0 or nc<0 or  nr == row or nc == col or (nr,nc) in seen:
                    continue
                seen.add((nr,nc))
                heapq.heappush(heap,(max(t,grid[nr][nc]),nr,nc))


