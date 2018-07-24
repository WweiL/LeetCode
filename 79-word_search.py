class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0:
            return word == ""
        else:
            marked = [[False] * len(board[0]) for i in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.word_search(i, j, 0, board, word, marked):
                        return True
            return False
    
    def word_search(self, i, j, k, board, word, marked):
        m = len(board)
        n = len(board[0])
        l = len(word)
        print("On " + str(i) + " " + str(j) + " word progress: " + str(k))
        print("board word: " + board[i][j])
        print("word word:  " + word[k])
        print("marked: ", marked)
        if word[k] != board[i][j] or marked[i][j] == True:
            return False
        elif k == l-1:
            return True
        else:
            marked[i][j] = True
            # Pruning
            if i < m-1 and self.word_search(i+1, j, k+1, board, word, marked):
                return True
            elif j < n-1 and self.word_search(i, j+1, k+1, board, word, marked):
                return True
            elif i > 0 and self.word_search(i-1, j, k+1, board, word, marked):
                return True
            elif j > 0 and self.word_search(i, j-1, k+1, board, word, marked):
                return True
            else:
                # TIL:
                # Python uses pass by object-reference
                # which means if you just assign the parameter to something,
                # the modification won't be reflected to the caller
                # But when you are modifying the parameter inplace, the param will
                # change even in the caller function
                marked[i][j] = False
                return False
