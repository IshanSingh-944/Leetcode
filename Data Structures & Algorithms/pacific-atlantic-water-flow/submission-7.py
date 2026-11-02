class Solution:
    def pacificAtlantic(self, h: List[List[int]]) :
        row = len(h)
        col = len(h[0])
        pq = deque()
        pseen = set()

        aq = deque()
        aseen = set()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(col):
            pq.append((0,i))
            pseen.add((0,i))
        for j in range(row):
            pq.append((j,0))
            pseen.add((j,0))
        
        for i in range(col):
            aq.append((row-1,i))
            aseen.add((row-1,i))
        for j in range(row-1):
            aq.append((j,col - 1))
            aseen.add((j,col - 1))

        def inte(q , seen):
            while q:
                r , c = q.popleft()
                for dr , dc in dir:
                    nr = dr + r
                    nc = dc + c
                    if 0<=nr<row and 0<=nc<col and h[nr][nc]>=h[r][c] and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        q.append((nr,nc))
        inte(pq,pseen)
        inte(aq,aseen)
        return list(pseen.intersection(aseen))


