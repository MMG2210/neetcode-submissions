class DisjointSet:
        
        def __init__(self, n: int):
            self.parent = list(range(n))
            self.rank = [0] * n
            self.components = n
        
        def find(self, node: int) -> int:
            if self.parent[node] != node:
                self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, u: int, v: int) -> bool:
            root_u, root_v = self.find(u), self.find(v)
            if root_u == root_v:
                return False
            
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                self.rank[root_v] += 1
            self.components -= 1
            
            return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DisjointSet(len(edges)+1)

        for edge in edges:
            u, v = edge

            if not dsu.union(u, v):
                return edge

        return []