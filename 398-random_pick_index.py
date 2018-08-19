import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dic = {}
        n = len(nums)
        i = 0
        while i < n:
            v = nums[i]
            self.dic[v] = [i, i]
            while i+1 < n and nums[i+1] == v:
                self.dic[v][1] += 1
                i += 1
            i += 1

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        low, hi = self.dic[target]
        if low == hi:
            return low
        else:
            return random.randint(low, hi)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
