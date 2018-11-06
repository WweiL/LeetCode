class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
    # Use stack to solve pairing bracket problems
        stack = []
        for e in s:
            if e != "]":
                stack.append(e)
            else:
                temp = ""
                while True:
                    if stack[-1] == "[":
                        stack.pop()
                    elif stack[-1].isdigit():
                        repeat_times = ""
                        while len(stack) != 0 and stack[-1].isdigit():
                            repeat_times = stack.pop() + repeat_times
                        stack.append(int(repeat_times) * temp)
                        break
                    else: # letter
                        temp = stack.pop() + temp

        return "".join(stack)

    class Solution:
        # recursive
#     def decodeString(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         i, n = 0, len(s)
#         ans = ""
#         while i < n:
#             c = s[i]
#             if c.isdigit():
#                 # first get number
#                 num = 0
#                 while s[i].isdigit(): 
#                     num = num*10 + int(s[i])
#                     i += 1
#                 # j is at '['
#                 j, balance = i+1, 1
#                 while j < n and balance > 0:
#                     if s[j] == '[': balance += 1
#                     if s[j] == ']': balance -= 1
#                     j += 1
#                 substr = self.decodeString(s[i+1: j-1])
#                 ans += num * substr
#                 i = j
#             else:
#                 ans += c
#                 i += 1
            
#         return ans
    # iterative, using stack
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = ""
        i, n = 0, len(s)
        currStr = ""
        while i < n:
            c = s[i]
            if c.isdigit():
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(currStr)
                stack.append(num)
                currStr = ""
            elif c == ']':
                num = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + num * currStr 
            else:
                currStr += c
            i += 1
        return currStr
