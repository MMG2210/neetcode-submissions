class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue, INF, directions = deque(), (2**31) - 1, [(1,0), (-1, 0), (0, 1), (0, - 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        
        while queue:
            for _ in range(len(queue)):
                x, y, dist = queue.popleft()

                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy

                    if (0 <= new_x < len(grid) and
                        0 <= new_y < len(grid[0]) and
                        grid[new_x][new_y] == INF
                        ):
                        grid[new_x][new_y] = dist + 1
                        queue.append((new_x, new_y, dist + 1))