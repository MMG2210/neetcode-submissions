class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        min_heap, total_cost = [(0,0)], 0

        while min_heap:
            cost, index = heapq.heappop(min_heap)
            if index in visited:
                continue
            
            visited.add(index)
            total_cost += cost
            u = points[index]

            for i, v in enumerate(points):
                if i in visited:
                    continue
                heapq.heappush(min_heap, (abs(v[0]-u[0]) + abs(v[1]-u[1]), i))
        
        return total_cost
