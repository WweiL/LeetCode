class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.word = ''

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]: return []
        self.trieHeads = {}
        for w in words:
            self.buildTrie(w)
        #for w in self.trieHeads:
        #    self.printTrie(self.trieHeads[w])
        ans, self.nRow, self.nCol = [], len(board), len(board[0])
        for r in range(self.nRow):
            for c in range(self.nCol):
                visited = [[False]*self.nCol for _ in range(self.nRow)]
                ans += self.findWord(board, r, c, visited, self.trieHeads)
        return list(set(ans))
    
    def findWord(self, board, r, c, visited, currDict):
        if board[r][c] not in currDict: return []
        node = currDict[board[r][c]]
        ans = []
        if node.word != '':
            ans += [node.word]
        visited[r][c] = True
        neighbors = []
        for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if row >= 0 and col >= 0 and row < self.nRow and col < self.nCol and (not visited[row][col]):
                neighbors.append((row, col))
        
        for row, col in neighbors:
            ans += self.findWord(board, row, col, visited, node.children)
        visited[r][c] = False
        return ans 
    
    def printTrie(self, node):
        if not node: return
        print("node.val: ", node.val, "node.addr", node)
        if node.word != '':
            print(node.word)
            print('---------')
        for child in node.children:
            self.printTrie(node.children[child])
            
    def buildTrie(self, word):
        head = self.trieHeads
        n = None
        for letter in word:
            if letter not in head:
                n = Node(letter)
                head[letter] = n
            else:
                n = head[letter]
            head = n.children
        n.word = word
