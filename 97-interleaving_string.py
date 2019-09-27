class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if (len(s3) != l1 + l2): return False
        if l2 > l1: return self.isInterleave(s2, s1, s3)
        dp = [False] * (l2+1)
        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if i == l1 and j == l2:
                    dp[l2] = True
                elif i == l1 and j != l2:
                    dp[j] = s2[j] == s3[i+j] and dp[j+1]
                elif i != l1 and j == l2:
                    dp[j] = s1[i] == s3[i+j] and dp[j]
                else:
                    dp[j] = (s2[j] == s3[i+j] and dp[j+1]) or (s1[i] == s3[i+j] and dp[j])
        return dp[0]
    
    # dp with 2d memory
    def isInterleave_dp2d(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if (len(s3) != l1 + l2): return False
        # dp[i][j] -> if s3 ending at [i+j] is a interleaving of s1 ending at [i] and s2 ending at [j]
        dp = [[False]*(l2+1) for _ in range(l1+1)]
        
        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if j == l2 and i == l1:
                    dp[i][j] = True
                elif j == l2 and i != l1:
                    dp[i][j] = s1[i] == s3[i+j] and dp[i+1][j] 
                elif j != l2 and i == l1:
                    dp[i][j] = s2[j] == s3[i+j] and dp[i][j+1]
                else:
                    dp[i][j] = (s1[i] == s3[i+j] and dp[i+1][j]) or (s2[j] == s3[i+j] and dp[i][j+1])
        return dp[0][0]
    
    # recursion with memoization
    def isInterleave_memo(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if len(s3) != l1 + l2: return False
        trace = [[-1]*(l2+1) for _ in range(l1+1)]
        trace[l1][l2] = 1
        return self.helper(s1, 0, s2, 0, s3, trace)
    
    def helper(self, s1: str, i: int, s2: str, j: int, s3: str, trace: List[List[int]]) -> bool:
        if trace[i][j] != -1: return True if trace[i][j] == 1 else False
        match = False
        if i != len(s1):
            match |= s1[i] == s3[i+j] and self.helper(s1, i+1, s2, j, s3, trace)
        if j != len(s2):
            match |= s2[j] == s3[i+j] and self.helper(s1, i, s2, j+1, s3, trace)
        trace[i][j] = 1 if match == True else 0
        return match
    
    # recursion TLE
    def isInterleave_recursion(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        # return True if s1 and s2 is a interleaving of s3
        if len(s2) == 0 and len(s1) == 0:
            return True
        match = False
        if len(s2) != 0:
                match |= s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:])
        if len(s1) != 0:
                match |= s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:])
        return match
