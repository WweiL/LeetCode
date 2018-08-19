class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        import collections
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        dic = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                dic[i+j].append(matrix[i][j])

        ans = []
        for i in range(m+n-1):
            l = dic[i]
            if not i % 2:
                l.reverse()
            ans += l

        return ans
