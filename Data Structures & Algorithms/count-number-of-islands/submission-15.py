class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        row = len(grid)
        col = len(grid[0])
        seen = set()
        def dfs(r,c):
            if r<0 or c<0 or r == row or c == col or grid[r][c]=='0' or (r,c) in seen:
                return 
            seen.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j]!= '1' or (i,j) in seen:
                    continue
                dfs(i,j)
                island +=1
        return island
