class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # O(n) time, O(1) space
        m, n = len(S), len(T)
        def getCount(s):
            count = 0
            for i in s:
                if count > 0 and i == '#':
                    count -= 1
                elif i != '#':
                    count += 1
            return count
        
        count = getCount(S)
        if count != getCount(T):
            return False
        i, j = m-1, n-1
        rem_i, rem_j = 0, 0
        for k in range(count):
            while rem_i != 0:
                if S[i] == '#':
                    rem_i += 1
                else:
                    rem_i -= 1
                i -= 1
            while rem_j != 0:
                if T[j] == '#':
                    rem_j += 1
                else:
                    rem_j -= 1
                j -= 1
            if S[i] != T[j]:
                return False
        return True
    # def backspaceCompare(self, S, T):
    #     """
    #     :type S: str
    #     :type T: str
    #     :rtype: bool
    #     """
    #     # O(n) time, O(n) space
    #     def getRes(s):
    #         stack = []
    #         for i in s:
    #             if stack and i == '#':
    #                 stack.pop()
    #             elif i != '#':
    #                 stack.append(i)
    #         return stack
    #     return getRes(S) == getRes(T)
