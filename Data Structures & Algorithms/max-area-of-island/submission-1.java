class Solution {
    private class DisjointSet{
        private int[] parent, size;
        private int SIZE;

        public DisjointSet(int SIZE){
            this.SIZE = SIZE;
            parent = new int[SIZE];
            size = new int[SIZE];

            for(int i = 0; i < SIZE; ++i){
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int findParent(int node){
            if(parent[node] != node){
                parent[node] = findParent(parent[node]);
            }
            return parent[node];
        }

        public boolean union(int u, int v){
            int parentU = findParent(u), parentV = findParent(v);
            
            if(parentU == parentV)
                return false;
            
            if(size[parentU] >= size[parentV]){
                size[parentU] += size[parentV];
                parent[parentV] = parentU;
            }
            else{
                size[parentV] += size[parentU];
                parent[parentU] = parentV;
            }
            return true;
        }

        public int getSize(int node){
            return size[findParent(node)];
        }
    }

    public int maxAreaOfIsland(int[][] grid) {
        int ROWS = grid.length, COLS = grid[0].length;
        DisjointSet dsu = new DisjointSet(COLS * ROWS);

        int[][] directions = new int[][]{{0,1}, {0,-1}, {1,0}, {-1,0}};
        int maxArea = 0;

        for(int row = 0; row < ROWS; ++row){
            for(int col = 0; col < COLS; ++col){
                if(grid[row][col] == 1){
                    for(int[] dir : directions){
                        int nrow = row + dir[0], ncol = col + dir[1];
                        if(nrow >= 0 && nrow < ROWS && ncol >= 0 && ncol < COLS && grid[nrow][ncol] == 1){
                            dsu.union(row * COLS + col, nrow * COLS + ncol);
                        }
                    }

                    maxArea = Math.max(maxArea, dsu.getSize(row * COLS + col));
                }
            }
        }

        return maxArea;
    }
}
