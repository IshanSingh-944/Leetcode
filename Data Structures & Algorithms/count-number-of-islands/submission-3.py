class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        row = len(grid)
        col = len(grid[0])
        seen = set()
        def dfs(startr,startc):
            stack = [(startr,startc)]
            seen.add((startr,startc))
            while stack :
                r,c = stack.pop()
                for dr , dc in dir:
                    nr = dr + r 
                    nc = dc + c
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1" and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        stack.append((nr,nc))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in seen:
                    cnt+=1
                    dfs(r,c)
        return cnt 
