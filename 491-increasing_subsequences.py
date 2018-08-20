# class Solution:
#     def findSubsequences(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         import copy
#         res = []
#         n = len(nums)
#         def dfs(startPos, step, marked, ans, path):
#             path.append(nums[startPos])
#             marked.add(startPos)
#             if step == 0:
#                 ans.append(path)
#             else:
#                 for i in range(startPos+1, n):
#                     if not i in marked and nums[i] >= nums[startPos]:
#                         dfs(i, step-1, copy.copy(marked), ans, copy.copy(path))

#         for i in range(2, n+1):
#             for j in range(n-i+1):
#                 dfs(j, i-1, set(), res, [])
#         return [list(x) for x in set([tuple(y) for y in res])]
class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = {()}
        for num in nums:
            new_sub = subs.copy()
            for e in subs:
                if not e or e[-1]<=num:
                    print(new_sub, "a")
                    n = tuple([num])
                    new_sub.add(e+n)
                    print(new_sub, "b")
            subs = new_sub
        return [x for x in subs if len(x)>1]
                    
