class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def calcProb(i, j, k, prob):
            pos = []
            for ii in [1, -1]:
                for jj in [2, -2]:
                    pos.append((i+ii, j+jj))
                    pos.append((i+jj, j+ii))
            _prob = 0
            for p in pos:
                if 0 <= p[0] < N and 0 <= p[1] < N:
                    _prob += prob[k-1][p[0]][p[1]]
            return _prob/8
        
        prob = [[[1]*N for i in range(N)] for j in range(K+1)]
        for k in range(1, K+1):
            p = prob[k]
            for i in range(N):
                for j in range(N):
                    prob[k][i][j] = calcProb(i, j, k, prob)
 
        return prob[K][r][c]


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = {}
        return self.dfs(r, c, memo, K, N) / (8**K)
            
    def dfs(self, r: int, c: int, memo: dict, m: int, N: int) -> int:
        # return the number of valid moves starting in (r, c) with m moves left
        if not (r >= 0 and c >= 0 and r < N and c < N): return 0
        if m == 0: return 1
        if (r, c, m) in memo: return memo[(r, c, m)]
        if (r, N-1-c, m) in memo: return memo[(r, N-1-c, m)]
        if (N-1-r, c, m) in memo: return memo[(N-1-r, c, m)]
        if (N-1-r, N-1-c, m) in memo: return memo[(N-1-r, N-1-c, m)]
        moves = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
        valid_moves = 0
        for i, j in moves:
            valid = self.dfs(r+i, c+j, memo, m-1, N)
            valid_moves += valid
        memo[(r, c, m)] = valid_moves
        return valid_moves
