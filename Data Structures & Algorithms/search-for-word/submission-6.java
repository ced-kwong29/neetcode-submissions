class Solution {
    private boolean search(char[][] board, int r, int c, String word) {
        if (word.isEmpty()) {
            return true;
        }

        if (board[r][c] != word.charAt(0)) {
            return false;
        }

        if (word.substring(1).isEmpty()) {
            return true;
        }

        board[r][c] = ' ';
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : directions) {
            int newR = d[0] + r, newC = d[1] + c;
            if (0 <= newR && newR < board.length && 0 <= newC && newC < board[r].length && board[newR][newC] != ' ') {
                if (search(board, newR, newC, word.substring(1))) {
                    return true;
                }
            }
        }
        board[r][c] = word.charAt(0);
        return false;
    }

    public boolean exist(char[][] board, String word) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[r].length; c++) {
                if (search(board, r, c, word)) {
                    return true;
                }
            }
        }
        return false;
    }
}
