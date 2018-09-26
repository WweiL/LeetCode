# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # greedy
        if not intervals:
            return 0
        intervals.sort(key=lambda d: d.start)
        end = intervals[0].end
        erased = 0
        for i in intervals[1:]:
            if i.start < end:
                erased += 1
                end = min(i.end, end)
            else:
                end = i.end
        return erased
#         # dp is good, but TLE
#         def overlap(i, j):
#             # assume i < j, intervals is sorted
#             return intervals[i].end > intervals[j].start
        
#         if not intervals:
#             return 0
#         n = len(intervals)
#         dp = [1] * n
#         ans = 1
#         intervals.sort(key=lambda d: d.start)
        
#         for i in range(n-2, -1, -1):
#             max_remained = 0
#             for j in range(i+1, n):
#                 if not overlap(i, j):
#                     max_remained = max(max_remained, dp[j]+1)

#             dp[i] = max_remained
#             ans = max(ans, dp[i])
#         return n - ans
