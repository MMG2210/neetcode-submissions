class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_time = [1e9] * (n+1)
        min_time[0] = 0
        adj_list = defaultdict(list)

        for u, v, time_taken in times:
            adj_list[u].append((v, time_taken))
        
        queue = deque([(k, 0)])
        min_time[k] = 0

        while queue:
            for _ in range(len(queue)):
                node, time_taken = queue.popleft()

                for child, time_needed in adj_list[node]:
                    new_time_taken = time_taken + time_needed
                    if new_time_taken < min_time[child]:
                        min_time[child] = new_time_taken
                        queue.append((child, new_time_taken))
        
        return max(min_time) if max(min_time) != 1e9 else -1
