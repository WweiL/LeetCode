class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
#         #cleaner:
#         summ = 0
#         d = {0: -1}
#         for i, num in enumerate(nums):
#             summ += num
#             if k != 0:
#                 summ %= k
#             if summ not in d:
#                 d[summ] = i
#             elif i - d[summ] >= 2:
#                 return True
        
#         return False
        n = len(nums)
        if k == 0:
            for i in range(n-1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False
        
        
        rem = n * [nums[0] % k]
        for i in range(1, n):
            rem[i] = (rem[i-1] + nums[i]) % k
            # in case of [0, 0], -1
            # if rem[i] == 0 and rem[i-1] == 0:
                # return True
                
        dic = {0: -1}
        for i in range(n):
            if rem[i] not in dic:
                dic[rem[i]] = i
            elif i - dic[rem[i]] > 1:
                    return True
        return 0 in dic and dic[0] != -1
