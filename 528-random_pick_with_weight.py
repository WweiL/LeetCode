class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        n = len(w)
        self.sums = [0] * n
        self.sums[0] = w[0]
        for i in range(1, n):
            self.sums[i] = self.sums[i-1] + w[i]
        # [2, 3, 4, 5]
        # [0, 1, 2, 3]
        # [2, 5, 9, 14]
        # random pick in [1, 14] call it P
        # [1, 2] -> 0
        # [3, 4, 5] -> 1
        # [6, 7, 8, 9] -> 2
        # [10, 11, 12, 13, 14] -> 3
        # find the smallest element in array that is greater than or eq to P
        # return index + 1

    def pickIndex(self):
        """
        :rtype: int
        """
        p = random.randint(1, self.sums[-1])
        l, r = 0, len(self.sums)-1
        while l < r:
            mid = l + r >> 1
            if self.sums[mid] >= p:
                r = mid
            else:
                l = mid + 1
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
