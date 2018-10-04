class Solution:
    # BFS, V: O(n), E: O(n) (1 + 1/4 + 1/9 + ... < 2)
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from collections import deque
        root = int(n**0.5)
        squares = [1] * (root+1)
        for i in range(root+1):
            squares[i] = i**2
            
        step = [-1]*(n+1)
        step[0] = 0
        q = deque()
        q.append(0)
        s = 0
        while q:
            #s += 1 # or use dict
            curr = q.popleft()
            for j in squares[1:]:
                neighbor = curr + j
                if neighbor > n:
                    break
                if neighbor == n:
                    return step[curr] + 1
                if neighbor < n and step[neighbor] == -1:
                    step[neighbor] = step[curr] + 1
                    q.append(neighbor)
        #return step[n]
                
            
            
    # DP, O(n^1.5), TLE in Python
    # def numSquares(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     def isSquare(n):
    #         return int(n**0.5) ** 2 == n
    #     dp = (n+1) * [float('inf')]
    #     dp[2] = 2
    #     dp[3] = 3
    #     for i in range(4, n+1):
    #         if(isSquare(i)):
    #             dp[i] = 1
    #         else:
    #             for k in range(1, int(i ** 0.5)+1):
    #                 dp[i] = min(1+dp[i-k**2], dp[i])
    #     return dp[n]
