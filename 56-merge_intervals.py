# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda d: d.start)
        ans = []
        i = 0
        while i < len(intervals):
            start = intervals[i].start
            end = intervals[i].end
            
            j = i
            while j < len(intervals) and intervals[j].start <= end:
                end = max(intervals[j].end, end)
                j += 1
            
            ans.append([start, end])
            i = j
        return ans
