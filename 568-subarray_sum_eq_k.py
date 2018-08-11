class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    
        sum_cnt = {0:1}
        s = 0
        counter = 0
        for i in range(len(nums)):
            s += nums[i]
            counter += sum_cnt.get(s-k, 0)
            sum_cnt[s] = sum_cnt.get(s, 0) + 1
                 
        return counter

# # only works if nums[i] > 0
# class Solution(object):
#     def subarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         if nums == None or nums == [] or k == 0:
#             return 0
#         counter = 0
#         s = 0
#         start = end = 0
#         while end < len(nums):
#             s += nums[end]
#             end += 1
#
#             while s > k:
#                 s -= nums[start]
#                 start += 1
#                 # if nums[i] > k
#                 print(start, end, len(nums))
#                 if start == end: break
#
#             if s == k:
#                 counter += 1
#
#
#         return counter
