class Solution:
    # best
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = len(matrix) - 1
        j = 0
        col = len(matrix[0])
        while i >= 0 and j < col:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

    # my optimized binary search, fast but not enough O(alogb), a = max(m, n), b = min(m, n)
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         def bin_search_horizontal(matrix, i, target):
#             row = matrix[i]
#             left = 0
#             right = len(row) - 1
#             if row[left] > target or row[right] < target:
#                 return False
#             while left < right:
#                 mid = (left+right) // 2
#                 if row[mid] == target:
#                     return True
#                 elif row[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
#             return row[left] == target
        
#         def bin_search_vertical(matrix, i, target):
#             up = 0
#             down = len(matrix) - 1
#             if(matrix[up][i] > target or matrix[down][i] < target):
#                 return False
#             while up < down:
#                 mid = (up+down) // 2
#                 if matrix[mid][i] == target:
#                     return True
#                 elif matrix[mid][i] < target:
#                     up = mid + 1
#                 else:
#                     down = mid
#             return matrix[up][i] == target

#         if not matrix:
#             return False
#         m = len(matrix)
#         n = len(matrix[0])
#         if m <= n:
#             for i in range(m):
#                 if bin_search_horizontal(matrix, i, target):
#                     return True
#         else:
#             for i in range(n):
#                 if bin_search_vertical(matrix, i, target):
#                     return True
#         return False
