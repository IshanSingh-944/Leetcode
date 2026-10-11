class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        graph= defaultdict(list)
        for src,dest in pre:
            graph[src].append(dest)
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
            return False
        for i in range(n):
            if state[i]==0:
                if dfs(i):
                    return False
        return True
                
            
