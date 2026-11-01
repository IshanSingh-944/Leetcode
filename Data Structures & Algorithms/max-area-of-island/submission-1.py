class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        row,col = len(grid),len(grid[0])
        r,c = 0,0
        def dfs(r,c):
            if (r < 0 or r >= row or
                c < 0 or c >= col or 
                grid[r][c] == 0 or 
                (r,c) in seen):
                return 0
            seen.add((r,c))
            return (1 + dfs(r-1,c) +
            dfs(r+1,c)+
            dfs(r,c-1) +
            dfs(r,c+1))
        for i in range(row):
            for j in range(col):
                if (i,j) not in seen and grid[i][j] == 1:
                   
                    res = max(res,dfs(i,j))
                    dfs(i,j)
        return res 
