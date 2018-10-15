# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left = []
        right = []
        s = newInterval.start
        e = newInterval.end
        for i in intervals:
            if i.end < newInterval.start: # i.end < s, same
                left.append(i)
            elif i.start > newInterval.end: # i.start > e, same
                right.append(i)
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right
    # binary search, bad idea
#     def insert(self, intervals, newInterval):
#         """
#         :type intervals: List[Interval]
#         :type newInterval: Interval
#         :rtype: List[Interval]
#         """
#         if not intervals:
#             return [newInterval]
#         startIdx = self.binsearch(newInterval.start, intervals)
#         endIdx = self.binsearch(newInterval.end, intervals)
#         print(startIdx, endIdx)
#         mergedInterval = Interval(min(intervals[startIdx].start, newInterval.start), max(intervals[endIdx].end, newInterval.end))
#         ans = []
#         for i in range(len(intervals)):
#             if i < startIdx or i > endIdx:
#                 ans.append(intervals[i])
#             elif i == startIdx:
#                 ans.append(mergedInterval)
#         return ans
                
        
#     def binsearch(self, s, intervals):
#         # return the index of the first interval with start < newInterval.start
#         l = 0
#         r = len(intervals) - 1
#         mid = 0
#         while l <= r:
#             mid = (l+r) // 2
#             if intervals[mid].start <= s and intervals[mid].end >= s:
#                 break
#             elif intervals[mid].end < s:
#                 l = mid+1
#             else:
#                 r = mid-1
#         if s < intervals[mid].start and mid != 0:
#             mid -= 1
#         if s > intervals[mid].end:
#             mid += 1
#         return mid
