import collections
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        lastOP = '+'
        j = 0
        n = len(s)
        lastPos = 0
        sign = 1
        while j < n:
            i = s[j]
            if i == ' ':
                j += 1
                continue
            elif i.isdigit():
                start = j
                lastPos = j
                while j < n and s[j].isdigit():
                    j += 1
                last = int(s[start: j])
            else:
                if i == '+':
                    ans += sign * last
                    lastOP = i
                    sign = 1
                elif i == '-':
                    ans += sign * last
                    lastOP = i
                    sign = -1
                else:
                    last, j = self.mul(s, lastPos)
                j += 1
        if lastOP == '+':
            ans += last
        else:
            ans -= last
        return ans
            
    def mul(self, s, start):
        lastOP = '*'
        j = start
        n = len(s)
        ans = 1
        while j < n:
            i = s[j]
            if i == ' ':
                j += 1
                continue
            elif i.isdigit():
                start = j
                while j < n and s[j].isdigit():
                    j += 1
                digit = int(s[start: j])
                if lastOP == '*':
                    ans *= digit
                else:
                    ans //= digit
            else:
                if i in ['*', '/']:
                    lastOP = i
                    j += 1
                else:
                    j -= 1
                    break
        # print(ans, s[start])
        return ans, j
