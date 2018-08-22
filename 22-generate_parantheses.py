class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        ans = []
        self.para("", ans, n, 0, 0)
        return ans

    def para(self, s, ans, n, left, right):
        if right == n:
            ans.append(s)
        else:
            if left < n:
                self.para(s+"(", ans, n, left+1, right)
            if right < left:
                self.para(s+")", ans, n, left, right+1)
        
        
# WRONG!
# class Solution:
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         if n == 1:
#             return ["()"]
#         else:
#             ans = self.generateParenthesis(n-1)
#             res = set()
#             for i in ans:
#                 res.add("(" + i + ")")
#                 res.add("()" + i)
#                 res.add(i + "()")
#             return list(res)
