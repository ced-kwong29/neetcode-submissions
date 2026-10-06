class Solution {
    private void travelIsland(char[][] grid, int r, int c) {
        grid[r][c] = '0';
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (int[] d : directions) {
            int newR = d[0] + r, newC = d[1] + c;
            if (0 <= newR && newR < grid.length && 0 <= newC && newC < grid[0].length && grid[newR][newC] == '1') {
                travelIsland(grid, newR, newC);
            }
        }
    }

    public int numIslands(char[][] grid) {
        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == '1') {
                    travelIsland(grid, r, c);
                    count++;
                }
            }
        }

        return count;
    }
}
