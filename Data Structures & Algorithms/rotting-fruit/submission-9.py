class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        fresh = 0
        total = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] ==1:
                    fresh+=1
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dir: 
                    nr = dr+r
                    nc = dc+c
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 1 and grid[nr][nc] !=0:
                        grid[nr][nc] =2
                        fresh -=1
                        q.append((nr,nc))
            total +=1
        return total if fresh == 0 else -1
