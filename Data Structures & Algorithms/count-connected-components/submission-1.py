class DisjointSet:
    def __init__(self, n: int):
        self.size = n;
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, node: int) -> int:
        if node != self.parent[node]:
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
    
    def get_disjoint_set_count(self) -> int:
        return self.components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DisjointSet(n)

        for u, v in edges:
            dsu.union(u, v)
        
        return dsu.get_disjoint_set_count()