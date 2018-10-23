class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # fast O(n^3), generalized for all N
        nums.sort()
        print(nums)
        result = []
        self.NSum(4, target, nums, 0, len(nums), [], result)
        return result

    def NSum(self, N, target, nums, start, end, curr, result):
        # assume nums is sorted, nums[start, end)
        l = end-start
        if l < N or nums[start] * N > target or nums[end-1] * N < target:
            return
        if N == 2:
            left, right = start, end-1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append(curr + [nums[left], nums[right]])
                    left, right = left+1, right-1
                    while left < right and nums[left] == nums[left-1]:  left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(start, end):
                if i == start or (i > start and nums[i-1] != nums[i]):
                    self.NSum(N-1, target-nums[i], nums, i+1, end, curr+[nums[i]], result)
                
#         # slow O(n^3)
#         from collections import defaultdict
#         s = set(nums)
#         n = len(nums)
#         ans = set()
#         pos = defaultdict(set)
#         for i in range(n):
#             pos[nums[i]].add(i)

#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     val = target-nums[i]-nums[j]-nums[k]
#                     if val in s and len([p for p in pos[val] if p != i and p != j and p != k]) > 0:
#                             ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
#         return list(ans)
