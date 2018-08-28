class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        ans = []
        self.addr("", ans, 4, s, 0)
        return ans
    
    def addr(self, tmp, ans, numBlock, s, i):
        n = len(s)
        if numBlock == 0 and i == n:
            ans.append(tmp[:-1])
        else:
            if i < n and s[i] == '0':
                self.addr(tmp+'0.', ans, numBlock-1, s, i+1)
            for j in range(1, 4):
                if i+j <= n and int(s[i:i+j]) <= 255 and s[i] != '0':
                    self.addr(tmp+s[i:i+j]+".", ans, numBlock-1, s, i+j)
                    
