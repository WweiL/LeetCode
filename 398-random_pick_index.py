class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.num_idx = collections.defaultdict(list)
        # for i, v in enumerate(nums):
            # self.num_idx[v].append(i)
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # indicies = self.num_idx[target]
        # res = indicies[0]
        # for i in range(1, len(indicies)):
            # if random.choice(range(i+1)) == 0:
                # res = indicies[i]
        # return res
        res = 0
        cnt = 0
        for i in range(len(self.nums)):
            if self.nums[i] != target:
                continue
            else:
                cnt += 1
                if random.randint(1, cnt) == 1:
                    res = i
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
