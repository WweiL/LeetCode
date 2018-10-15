class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(self.trav(s), self.trav(self.reverse(s)))
        
    def trav(self, s):
        left, right, start = 0, 0, 0
        ans = 0
        for i, p in enumerate(s):
            if p == '(':
                left += 1
            if p == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
            if right > 0:
                right, left = 0, 0
                start = i+1
            elif left == 0 and i != 0: # right == 0
                ans = max(ans, i - start + 1)
        return ans

    def reverse(self, s):
        ans = []
        for i in reversed(s):
            if i == '(':
                ans.append(')')
            else:
                ans.append('(')
        return "".join(ans)
