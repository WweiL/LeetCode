class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        height = len(matrix)
        length = len(matrix[0])
        marked = [[False]*length for i in range(height)]
        ans = []
        i, j = 0, 0
        direction = 0
        # 0 -> right
        # 1 -> down
        # 2 -> left
        # 3 -> up
        while(True):
            up = i-1 if i-1 >= 0 else i
            down = i+1 if i+1 < height else i
            left = j-1 if j-1 >= 0 else j
            right = j+1 if j+1 < length else j
            ans.append(matrix[i][j])
            marked[i][j] = True
            if(sum([marked[up][j], marked[down][j], marked[i][left], marked[i][right]]) == 4):
                break
            if direction == 0:
                if right == j or marked[i][right]:
                    direction = 1
                    i = down
                else:
                    j = right
            elif direction == 1:
                if down == i or marked[down][j]:
                    direction = 2
                    j = left
                else:
                    i = down
            elif direction == 2:
                if left == j or marked[i][left]:
                    direction = 3
                    i = up
                else:
                    j = left
            else:
                if up == i or marked[up][j]:
                    direction = 0
                    j = right
                else:
                    i = up
        return ans
            
