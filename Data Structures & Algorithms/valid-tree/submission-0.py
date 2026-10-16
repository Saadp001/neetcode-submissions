class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n - 1 != len(edges):
            return False 

        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node, parent):
            visit[node] = 1

            for nei in adj[node]:
                if visit[nei] == 0:
                    if not dfs(nei, node):
                        return False

                elif nei != parent:
                    return False  

            return True              

        visit = [0]*n
        ans = 0
        for i in range(n):
            if visit[i] == 0:
                if dfs(i, -1):
                    ans+=1        

        return ans <= 1        