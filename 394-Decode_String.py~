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
