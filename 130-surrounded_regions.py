class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2: return
        if len(board[0]) <= 2: return
        m = len(board)
        n = len(board[0])
        def markDFS(i, j, board):
            if board[i][j] == 'S':
                return
            board[i][j] = 'S'
            up = i - 1 if i > 0 else 0
            down = i + 1 if i < m - 1 else m - 1
            left = j - 1 if j > 0 else 0
            right = j + 1 if j < n - 1 else n - 1
            for x, y in [(up, j), (down, j), (i, left), (i, right)]:
                if board[x][y] == 'O':
                    markDFS(x, y, board)
        
        for i in range(m):
            if i == 0 or i == m-1:
                for j in range(n):
                    if(board[i][j] == 'O'):
                        markDFS(i, j, board)
            else:
                for j in [0, n-1]:
                    if(board[i][j] == 'O'):
                        markDFS(i, j, board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
                
