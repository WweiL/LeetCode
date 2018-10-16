class Solution:
    from copy import copy
    # See notes for details of copy
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.'] * n for _ in range(n)]
        ans = []
        self.queens(0, board, ans)
        return ans

    def isvalid(self, board, i, j):
        n = len(board)
        for row in range(n):
            if row != i and board[row][j] == 'Q':
                return False
            diff = abs(row - i)
            if (j-diff >= 0 and board[row][j-diff] == 'Q') or (j+diff < n and board[row][j+diff] == 'Q'):
                return False
        return True

    def queens(self, row, board, ans):
        n = len(board)
        if row == n:
            for i in range(n):
                board[i] = "".join(board[i])
            ans.append(board)
        else:
            for col in range(n):
                if self.isvalid(board, row, col):
                    tmp = copy.copy(board)
                    tmp[row] = copy.copy(board[row])
                    tmp[row][col] = 'Q'
                    self.queens(row+1, tmp, ans)
