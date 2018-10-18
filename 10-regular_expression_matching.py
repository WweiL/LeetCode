class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def eq(a, b):
            return a == b or b == '.'
        
        m = len(s)
        n = len(p)
        # if m == 0:
            # return n % 2 == 0 and [p[i] for i in range(n) if i % 2 == 1] == ['*'] * (n//2)
        # if n == 0:
            # return m == 0
        p = p + "@@"
        s = s + "^^"
        reg = [[False]*(n+2) for _ in range(m+2)]
        reg[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n: continue
                if p[j+1] == '*' and eq(s[i], p[j]):
                    reg[i][j] = reg[i+1][j] or reg[i][j+2] or reg[i+1][j+2]
                if p[j+1] == '*' and not eq(s[i], p[j]):
                    reg[i][j] = reg[i][j+2]
                if p[j+1] != '*' and eq(s[i], p[j]):
                    reg[i][j] = reg[i+1][j+1]
                # if p[j+1] != '*' and not eq(s[i], p[j]):
                    # reg[i][j] = False
        return reg[0][0]
