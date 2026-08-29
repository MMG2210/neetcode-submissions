class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [1e9] * (n+1)
        adj_list = defaultdict(list)

        for u, v, time_taken in times:
            adj_list[u].append((v, time_taken))
        
        min_heap = [(0, k)]
        min_time[k] = 0

        while min_heap:
            time_taken, node = heapq.heappop(min_heap)

            for child, time_needed in adj_list[node]:
                new_time_taken = time_taken + time_needed
                if new_time_taken < min_time[child]:
                    min_time[child] = new_time_taken
                    heapq.heappush(min_heap, (new_time_taken, child))
        
        return max(min_time[1:]) if max(min_time[1:]) != 1e9 else -1
