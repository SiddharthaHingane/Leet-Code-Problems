class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u,v,d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
        def dfs(u):
            visited.add(u)
            for v,d in graph[u]:
                self.minScore = min(self.minScore, d)
                if v not in visited:
                    dfs(v)
        visited = set()
        self.minScore = float('inf')
        dfs(1)
        return self.minScore
