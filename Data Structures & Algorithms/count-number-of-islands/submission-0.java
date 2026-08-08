class Solution {
    private int[][] directions = new int[][]{{1,0}, {-1,0}, {0,1}, {0,-1}};
    private int m, n;

    private int dfs(char[][] grid, int row, int col){
        if(row < 0 || row == m || col < 0 || col == n || grid[row][col] == '0'){
            return 0;
        }
        int sizeOfIsland = 1;
        grid[row][col] = '0';

        for(int[] direction : directions){
            int newRow = row + direction[0], newCol = col + direction[1];
            sizeOfIsland += dfs(grid, newRow, newCol);
        }
        return sizeOfIsland;
    }

    public int numIslands(char[][] grid) {
        int numberOfIslands = 0;
        char[][] newGrid = Arrays.stream(grid).map(char[]::clone).toArray(char[][]::new);
        m = grid.length;
        n = grid[0].length;

        for(int i = 0; i < m; ++i){
            for(int j = 0; j < n; ++j){
                if(newGrid[i][j] == '1'){
                    dfs(newGrid, i, j);
                    numberOfIslands++;
                }
            }
        }

        return numberOfIslands;
    }
}
