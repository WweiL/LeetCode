class Solution:
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        n=len(nums)
        if n<7:
            return False
        
        leftsum = [0] * n
        leftsum[0] = nums[0]
        d = defaultdict(set)
        for i in range(1,n):
            leftsum[i] = leftsum[i-1] + nums[i]
            d[leftsum[i]].add(i)
        
        # sam = leftsum[i-1]
        # sam = leftsum[j-1]-leftsum[i]
        # sam = leftsum[k-1]-leftsum[j]
        # sam = leftsum[n-1]-leftsum[k]
        for i in range(1, n-5):
            sam = leftsum[i-1]
            if leftsum[n-1]-sam in d:       # find leftsum[k] in dict d through  leftsum[n-1]-sam
                for k in d[leftsum[n-1]-sam]:
                    if i+4<=k<=n-2:
                        # now we want to get j so that, leftsum[j-1]=leftsum[i]+sam, leftsum[j]=leftsum[k-1]-sam
                        t1=leftsum[i]+sam
                        t2=leftsum[k-1]-sam
                        if t1 in d and t2 in d:
                            if len(d[t1])>len(d[t2]):
                                for j in d[t2]:
                                    if j-1 in d[t1]:
                                        return True
                            else:
                                for j1 in d[t1]:
                                    if j1+1 in d[t2]:
                                        return True
        
        return False
#         from collections import defaultdict
#         n = len(nums)
#         if n < 7:
#             return False
#         sums = [0]*n
#         for i in range(n):
#             sums[i] = sums[i-1] + nums[i]
        
#         suffix = nums[n-1]
#         suffix_pos = defaultdict(set)
#         for i in range(n-2, -1, -1):
#             suffix_pos[suffix].add(i)
#             suffix += nums[i]

#         for j in range(3, n-3):
#             tmp_sum = set()
#             for i in range(1, j-1):
#                 if sums[i] - nums[i] == sums[j-1] - sums[i]:
#                     tmp_sum.add(sums[i] - nums[i])
#             for s in tmp_sum:
#                 for pos in suffix_pos[s]:
#                     if pos > j+1 and s == sums[pos] - nums[pos] - sums[j]:
#                         return True
#         return False
        return False
            # for k in range(j+2, n-1):
            #     s = sums[k] - nums[k] - sums[j]
            #     if s == sums[n-1] - sums[k] and s in tmp_sum:
            #         return True
        return False
