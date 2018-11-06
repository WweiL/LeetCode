class Solution:
    def __init__(self):
        self.fact = [1] * 10
        for i in range(1, 10):
            self.fact[i] = self.fact[i-1] * i
    
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        l = [1] * n
        for i in range(n):
            l[i] = i+1
        self.permHelper(l, k-1, ans)
        return "".join(ans)
    
    def permHelper(self, l, k, ans):
        # return the kth permutaion in l
        # by recursively calculating the first element
        # base case:
        n = len(l)
        if n == 1:
            ans.append(str(l[0]))
            return
        i = k // self.fact[n-1]
        ans.append(str(l[i]))
        self.permHelper(l[:i] + l[i+1:], k % self.fact[n-1], ans)
