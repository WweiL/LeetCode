class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        if n <= 2:
            return True
        inc = 0
        for i in range(n-1):
            if inc == 0 and A[i] < A[i+1]:
                inc = 1
            elif inc == 0 and A[i] > A[i+1]:
                inc = -1
            elif inc == 1 and A[i] > A[i+1]:
                return False
            elif inc == -1 and A[i] < A[i+1]:
                return False
        return True
