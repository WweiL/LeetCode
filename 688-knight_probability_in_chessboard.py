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
