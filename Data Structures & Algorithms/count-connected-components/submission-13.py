class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        def dfs(n):
            if n not in seen:
                seen.add(n)
            else:
                return
            for nei in graph[n]:
                dfs(nei)
        cnt = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                cnt+=1

        return cnt

