class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        seen = set()
        
        
        def dfs(r,c):
            if (r < 0 or r >= row or
                c < 0 or c >= col or 
                grid[r][c] == '0' or 
                (r,c) in seen):
                return 
            seen.add((r,c))
            dfs(r-1,c) 
            dfs(r+1,c)
            dfs(r,c-1) 
            dfs(r,c+1)
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in seen:
                    cnt+=1
                    dfs(i,j)
        return cnt


