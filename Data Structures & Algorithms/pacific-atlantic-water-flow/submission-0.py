class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        pacific, atlantic = set(), set()

        def dfs(row: int, col: int, ocean_set: set) -> None:
            ocean_set.add((row, col))

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if(0 <= new_row < m and 0 <= new_col < n and
                    (new_row, new_col) not in ocean_set and
                    heights[new_row][new_col] >= heights[row][col]):

                    dfs(new_row, new_col, ocean_set)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)
        
        return [list(cell) for cell in (pacific & atlantic)]
        