class Solution:
    # recursive, O(n) time, O(1) space
    # think every number as number * 1
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        add_minus, am_res = '+', 0
        mul_div, md_res = '*', 1
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c.isdigit():
                start = i
                while i+1 < n and s[i+1].isdigit():
                    i += 1
                num = int(s[start: i+1])
                md_res = (md_res * num) if mul_div == '*' else (md_res // num)
            elif c in ["*", "/"]:
                mul_div = c
            elif c in ['+', '-']:
                sign = 1 if add_minus == '+' else -1
                am_res += sign * md_res
                add_minus = c
                mul_div, md_res = '*', 1
            elif c == '(':
                j, cnt = i+1, 1
                while cnt != 0:
                    cnt += 1 if s[j] == '(' else 0
                    cnt -= 1 if s[j] == ')' else 0
                    j += 1
                num = self.calculate(s[i+1:])
                md_res = (md_res * num) if mul_div == '*' else (md_res // num)
                i = j-1
            elif c == ')':
                break
            i += 1
        sign = 1 if add_minus == '+' else -1
        return am_res + md_res * sign
# import collections
# class Solution:
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         ans = 0
#         lastOP = '+'
#         j = 0
#         n = len(s)
#         lastPos = 0
#         sign = 1
#         while j < n:
#             i = s[j]
#             if i == ' ':
#                 j += 1
#                 continue
#             elif i.isdigit():
#                 start = j
#                 lastPos = j
#                 while j < n and s[j].isdigit():
#                     j += 1
#                 last = int(s[start: j])
#             else:
#                 if i == '+':
#                     ans += sign * last
#                     lastOP = i
#                     sign = 1
#                 elif i == '-':
#                     ans += sign * last
#                     lastOP = i
#                     sign = -1
#                 else:
#                     last, j = self.mul(s, lastPos)
#                 j += 1
#         if lastOP == '+':
#             ans += last
#         else:
#             ans -= last
#         return ans
#
#     def mul(self, s, start):
#         lastOP = '*'
#         j = start
#         n = len(s)
#         ans = 1
#         while j < n:
#             i = s[j]
#             if i == ' ':
#                 j += 1
#                 continue
#             elif i.isdigit():
#                 start = j
#                 while j < n and s[j].isdigit():
#                     j += 1
#                 digit = int(s[start: j])
#                 if lastOP == '*':
#                     ans *= digit
#                 else:
#                     ans //= digit
#             else:
#                 if i in ['*', '/']:
#                     lastOP = i
#                     j += 1
#                 else:
#                     j -= 1
#                     break
#         # print(ans, s[start])
#         return ans, j
