class Solution {
    private int[][] directions = new int[][]{{1,0}, {-1,0}, {0,1}, {0,-1}};
    private int m, n;

    private int dfs(int[][] grid, int row, int col){
        if(row < 0 || row == m || col < 0 || col == n || grid[row][col] == 0){
            return 0;
        }
        int sizeOfIsland = 1;
        grid[row][col] = 0;

        for(int[] direction : directions){
            int newRow = row + direction[0], newCol = col + direction[1];
            sizeOfIsland += dfs(grid, newRow, newCol);
        }
        return sizeOfIsland;
    }

    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        m = grid.length;
        n = grid[0].length;

        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                if(grid[i][j] == 1){
                    res = Math.max(res, dfs(grid, i, j));
                }
            }
        }

        return res;
    }
}
