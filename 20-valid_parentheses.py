from collections import deque
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            stack = deque()
            stack.append(s[0])
            pair = {'{': '}', '[': ']', '(': ')', '}': '{', ']': '[', ')': '('}
            for w in s[1:]:
                if not stack or stack[-1] != pair[w]:
                    stack.append(w)
                else:
                    stack.pop()
            return not stack
