class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        dfs(0)
        return True if len(seen) == n else False

