class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        ans = ""
        k = 0
        i = len(S) - 1
        while i >= 0:
            if k == K:
                ans = "-"+ ans
                k = 0
            elif S[i] == '-':
                i -= 1
            else:
                ans = S[i] + ans
                k += 1
                i -= 1

        if ans and ans[0] == '-':
            ans = ans[1:]
        return ans.upper()
