class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        marked = [False]*n
        def dfs(i):
            marked[i] = True
            for j in range(n):
                if not marked[j] and M[i][j] == 1:
                    dfs(j)
        circles = 0
        for i in range(len(M)):
            if not marked[i]:
                circles += 1
                dfs(i)
        return circles
