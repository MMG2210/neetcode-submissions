class Solution:
    def get_dist(self, first: list[int], second: list[int]) -> int:
        return abs(first[0] - second[0]) + abs(first[1] - second[1])

    def get_disjoint_set_roots(self, edges: list) -> dict:
        roots = defaultdict(int)
        for u, v, dist in edges:
            roots[u] = u
            roots[v] = v
        return roots
    
    def find(self, node: int, roots: list) -> int:
        if roots[node] != node:
            roots[node] = self.find(roots[node], roots)
        return roots[node]

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = self.get_dist(points[i], points[j])
                edges.append((tuple(points[i]), tuple(points[j]), dist))
        edges.sort(key = lambda x : x[2])
        
        roots = self.get_disjoint_set_roots(edges)
        min_cost = 0
        for u, v, dist in edges:
            root_u, root_v = self.find(u, roots), self.find(v, roots)
            if root_u == root_v:
                continue
            min_cost += dist
            roots[root_u] = root_v
        
        return min_cost