# clever one
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        idx = step = 0
        res = [""] * numRows
        for c in s:
            res[idx] += c
            if idx == 0:
                step = 1
            elif idx == numRows-1:
                step = -1
            idx += step
        return "".join(res)

# stupid my own solution
# class Solution:
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1 or len(s) < numRows:
#             return s
#         s = "#" + s
#         n = numRows
#         res = [s[i] for i in range(1, n+1)]
        
#         # first row
#         i = 1
#         while True:
#             idx = 2*i*n-2*i+1
#             i += 1
#             if idx >= len(s):
#                 break
#             res[0] += s[idx]
            
#         for i in range(2, n):
#             j = 1
#             while True:
#                 first = (j+1) * n - i - j + 1
#                 second = (j+1) * n - i - j + 1 + 2 * (i-1)
#                 j += 2
#                 if first >= len(s):
#                     break
#                 if first < len(s):
#                     res[i-1] += s[first]
#                 if second < len(s):
#                     res[i-1] += s[second]
                    
#         # last row
#         i = 1
#         while True:
#             idx = (2*i+1)*n - 2*i
#             if idx >= len(s):
#                 break
#             res[n-1] += s[idx]
#             i += 1
#         return "".join(res)
