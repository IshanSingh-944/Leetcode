class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) :
        row = len(grid)
        col = len(grid[0])
        pq = deque()
        pseen = set()

        aq = deque()
        aseen = set()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(row):
            pq.append((i,0))
            pseen.add((i,0))
        for j in range(col):
            pq.append((0,j))
            pseen.add((0,j))

        for i in range(row):
            aq.append((i,col-1))
            aseen.add((i,col-1))
        for j in range(col):
            aq.append((row-1,j))
            aseen.add((row-1,j))
        
        def bfs(q,seen):
            while q:
                r,c = q.popleft()
                for dr,dc in dir:
                    nr = dr+r
                    nc = dc+c
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]>=grid[r][c]and (nr,nc) not in seen:
                        q.append((nr,nc))
                        seen.add((nr,nc))
        bfs(pq,pseen)
        bfs(aq,aseen)
        return list(pseen.intersection(aseen))
        
