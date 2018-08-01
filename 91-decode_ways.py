class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" or "00" in s:
            return 0

        n = len(s)
        # Facilitate indexing
        s = "#" + s
        res = [None] * (n+2)
        res[-1] = 1
        # Base case: res[-2] and res[-3]
        # Setting res[-1] to 1 to simplify code as well as handle the case of index out of bound in line 31
        res[-2] = 1 if s[-1] != "0" else 0
        for i in range(n-1, 0, -1):
            if s[i] == "0":
                res[i] = 0
            else:
                num = int(s[i:i+2])
                if num > 26:
                    res[i] = res[i+1]
                else:
                    res[i] = res[i+1] + res[i+2]
        return res[1]
# class Solution:
#     def numDecodings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if "00" in s:
#             return 0
#
#         n = len(s)
#         if n == 0:
#             return 0
#         if n == 1:
#             return 0 if s == "0" else 1
#
#         s = "#" + s
#         res = [None] * (n+1)
#         # Base case: res[-1] and res[-2]
#         res[-1] = 1 if s[-1] != "0" else 0
#         # res[-2]
#         if s[-2] == "0":
#             res[-2] = 0
#         else:
#             num = int(s[-2]+s[-1])
#             if num > 26:
#                 if num % 10 == 0:
#                     res[-2] = 0
#                 else:
#                     res[-2] = 1
#             elif num == 20 or num == 10:
#                 res[-2] = 1
#             else:
#                 res[-2] = 2
#         for i in range(n-2, 0, -1):
#             if s[i] == "0":
#                 res[i] = 0
#             else:
#                 num = int(s[i] + s[i+1])
#                 if num > 26:
#                     res[i] = res[i+1]
#                 else:
#                     res[i] = res[i+1] + res[i+2]
#         return res[1]
