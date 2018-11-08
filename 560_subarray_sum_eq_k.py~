

# only works if nums[i] > 0
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # two-pass
        from collections import defaultdict
#         if nums == None or nums == []:
#             return 0
#         n = len(nums)
#         prefix_sums = [0] * n
#         sum_pos = defaultdict(list)
#         sum_pos[0] = [-1]
#         for i in range(n):
#             # prefix_sums[-1] = 0, wrap back
#             prefix_sums[i] = prefix_sums[i-1] + nums[i]
#             sum_pos[prefix_sums[i]].append(i)

#         count = 0
#         for i, v in enumerate(prefix_sums):
#             if v-k in sum_pos:
#                 for pos in sum_pos[v-k]:
#                     if pos < i:
#                         count += 1
#         return count
        # ------------------------------------------------------------------------------------------------------------
        # better, one-pass
        # O(n) space, time
        # if nums == None or nums == []:
        #     return 0
        # sum_pos = defaultdict(list)
        # sum_pos[0] = [-1]
        # count = 0
        # prefix_sum = 0
        # for i in range(len(nums)):
        #     prefix_sum += nums[i]
        #     sum_pos[prefix_sum].append(i)
        #     if prefix_sum-k in sum_pos:
        #         for pos in sum_pos[prefix_sum-k]:
        #             if pos < i:
        #                 count += 1
        # return count
        
        # ------------------------------------------------------------------------------------------------------------
        # O(n**2) time, O(1) space
        # prefix_sum = 0
        # cnt = 0
        # n = len(nums)
        # for i in range(n):
        #     # prefix_sum += nums[i]
        #     sum_tmp = prefix_sum
        #     for j in range(i, n):
        #         sum_tmp += nums[j]
        #         if sum_tmp == k:
        #             cnt += 1
        # return cnt
