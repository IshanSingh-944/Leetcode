class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for  u, v in p:
            graph[u].append(v)
        ans = []
        state = [0]*n
        def dfs(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False
            state[node] = 1
            for nei in graph[node]:
                if dfs(nei):
                    return True
            state[node] = 2
            ans.append(node)
            return False
        for ot in range(n):
            if state[ot] == 0:
                if dfs(ot):
                    return []
        return ans