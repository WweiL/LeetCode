class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                s = nums[lo] + nums[i] + nums[hi]
                if s < 0:
                    lo += 1
                elif s > 0:
                    hi -= 1
                else:
                    ans.append([nums[lo], nums[i], nums[hi]])
                # eliminate duplication
                    while lo < hi and nums[lo+1] == nums[lo]:
                        lo += 1
                    while lo < hi and nums[hi-1] == nums[hi]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        return ans
# wrong
# class Solution:
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         nums.sort()
#         from collections import defaultdict
#         idx = defaultdict(list)
#         n = len(nums)
#         for i in range(n):
#             idx[-nums[i]].append(i)
        
#         ans = []
#         passed = set()
#         for i in range(n):
#             for j in range(i+1, n):
#                 # if i == j:
#                     # continue
#                 s = nums[i] + nums[j]
#                 if s in idx:
#                     for _idx in idx[s]:
#                         if _idx != i and _idx != j:
#                             if not _idx in passed or not i in passed or not j in passed:
#                                 ans.append([nums[i], nums[j], nums[_idx]])
#                                 passed.add(i)
#                                 passed.add(j)
#                                 passed.add(_idx)
#         return list([list(i) for i in set([tuple(i) for i in ans])])
                    
