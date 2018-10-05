from copy import copy
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.getInvalidNum(s)
        if self.left == 0 and self.right == 0:
            return [s]
        ans = set()
        self.para(s, 0, 0, 0, ans, [], 0)
        return list(ans)
        
    def para(self, s, idx, left, right, ans, tmp, cnt):
        if idx == len(s):
            if left == self.left and right == self.right:
                ans.add("".join(tmp))
        else:
            if left <= self.left and right <= self.right and cnt >= 0:
                if s[idx] != '(' and s[idx] != ')':
                    tmp.append(s[idx])
                    self.para(s, idx+1, left, right, ans, copy(tmp), cnt)
                else:
                    if s[idx] == '(':
                        self.para(s, idx+1, left+1, right, ans, copy(tmp), cnt)
                        tmp.append(s[idx])
                        self.para(s, idx+1, left, right, ans, copy(tmp), cnt+1)
                    else:
                        self.para(s, idx+1, left, right+1, ans, copy(tmp), cnt)
                        tmp.append(s[idx])
                        self.para(s, idx+1, left, right, ans, copy(tmp), cnt-1)
                    
    
    def getInvalidNum(self, s):
        left = 0
        right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1
        self.left = left
        self.right = right
