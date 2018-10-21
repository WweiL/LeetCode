class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(1) space, better
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0
        # O(n) time, space, not good
#         return self.valid(s) and self.valid(self.reverse(s))
    
#     def reverse(self, s):
#         s = s[::-1]
#         ret = []
#         for i in range(len(s)):
#             if s[i] == '(':
#                 ret.append(')')
#             elif s[i] == ')':
#                 ret.append('(')
#             else:
#                 ret.append('*')
#         return "".join(ret)

#     def valid(self, s):
#         left = 0
#         star = 0
#         for p in s:
#             if p == '(':
#                 left += 1
#             elif p == ')':
#                 if left > 0:
#                     left -= 1
#                 elif star > 0:
#                     star -= 1
#                 else:
#                     return False
#             else:
#                 star += 1
#         return True
