class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix is None or not matrix:
            return
        self.height = len(matrix)
        self.length = len(matrix[0])
        self.mem = [[0] * (self.length+1) for _ in range(self.height+1)]
        
        for i in range(self.height-1, -1, -1):
            self.mem[i][self.length-1] = self.mem[i+1][self.length-1] + matrix[i][self.length-1]
        for i in range(self.length-1, -1, -1):
            self.mem[self.height-1][i] = self.mem[self.height-1][i+1] + matrix[self.height-1][i]
            
        for i in range(self.height-2, -1, -1):
            for j in range(self.length-2, -1, -1):
                self.mem[i][j] = matrix[i][j] + self.mem[i][j+1] + self.mem[i+1][j] - self.mem[i+1][j+1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        down = self.mem[row1][col2+1]
        right = self.mem[row2+1][col1]
        dr = self.mem[row2+1][col2+1]
        return self.mem[row1][col1] - down - right + dr


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
