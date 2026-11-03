class Solution:
    def countComponents(self, n: int, edges: List[List[int]]):
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        cnt = 0
        start = 0
        
        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr in seen:
                    continue
                seen.add(curr)
                for nei in graph[curr]:
                    if nei not in seen:
                        
                        stack.append(nei)
        for i in range(n):
            if i not in seen:
                cnt+=1
                dfs(i)
        return cnt

            