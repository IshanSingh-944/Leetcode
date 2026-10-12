class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        cnt = 0
        def dfs(node):
            if node not in seen:
                seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        for i in range(n):
            if i not in seen:
                dfs(i)
                cnt+=1
        return cnt



            