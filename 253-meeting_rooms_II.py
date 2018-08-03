# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        if intervals == [] or not intervals:
            return 0
        intervals = sorted(intervals, key = lambda d: d.start)
        endheap = [intervals[0].end]
        
        rooms = 1
        for i in range(1, len(intervals)):
            if endheap and endheap[0] > intervals[i].start:
                rooms += 1
            elif endheap and endheap[0] <= intervals[i].start:
                heapq.heappop(endheap)
            heapq.heappush(endheap, intervals[i].end)
        return rooms
        
# class Solution:
#     def minMeetingRooms(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: int
#         """
#         if intervals == []:
#             return 0
        
#         starts = []
#         ends = []
#         for i in intervals:
#             starts.append(i.start)
#             ends.append(i.end)
#         starts.sort()
#         ends.sort()
        
#         s = e = 0
#         numNeeded = numAvailable = 0
#         while s < len(starts):
#             if starts[s] < ends[e]:
#                 if numAvailable == 0:
#                     numNeeded += 1
#                 else:
#                     numAvailable -= 1
                    
#                 s += 1
#             else:
#                 numAvailable += 1
#                 e += 1
        
#         return numNeeded
