class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        fresh, timeElapsed = 0, 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        while queue and fresh > 0:
            queueSize = len(queue)

            for _ in range(queueSize):
                row, col = queue.popleft()

                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]

                    if(0 <= new_row < m and 0 <= new_col < n and 
                        grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))
            
            timeElapsed += 1
        
        return timeElapsed if fresh == 0 else -1