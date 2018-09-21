class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        step = [0] * n
        step[n-1] = 1
        step[n-2] = 2
        for i in range(n-3, -1, -1):
            step[i] = step[i+1] + step[i+2]
        return step[0]
        
