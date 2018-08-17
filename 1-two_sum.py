class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        d = {}
        for i, v in enumerate(nums):
            if d.get(target-v, -1) != -1:
                ans.append(d[target-v])
                ans.append(i)
            d[v] = i
        return ans
            
