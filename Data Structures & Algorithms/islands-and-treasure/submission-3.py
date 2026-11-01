class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            r,c = q.popleft()
            for dr,dc in dir:
                nr = dr+r
                nc = dc+c
                if nr<0 or nc<0 or nr >= row or nc >= col or grid[nr][nc]!=2147483647:
                    continue
                grid[nr][nc] = 1+grid[r][c]
                q.append((nr,nc))
        