# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda d: d.start)
        endheap = [intervals[0].end] # stores current meetings, meetings not ended yet
        n = len(intervals)
        rooms = 1
        for i in range(1, n):
            if endheap:
                if intervals[i].start < endheap[0]: # 
                    rooms += 1
                else: # intervals[i].start >= endheap[0]:
                    heapq.heappop(endheap)
            heapq.heappush(endheap, intervals[i].end)
        return rooms 

    def minMeetingRooms3(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        cnt = collections.defaultdict(int)
        for i in intervals:
            cnt[i.start] += 1
            cnt[i.end] -= 1
        rooms = 0
        ans = 0
        for v in [cnt[i] for i in sorted(cnt)]: # sort according to time
            ans += v
            rooms = max(ans, rooms)
        return rooms

    def minMeetingRooms2(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        rooms, avail, n = 0, 0, len(intervals)
        startIdx, endIdx = 0, 0 
        while startIdx < n:
            if start[startIdx] < end[endIdx]: # when a new meeting starts, the current last meeting has not ended
                if avail == 0:
                    rooms += 1
                else:
                    avail -= 1
                startIdx += 1 # proceed to next meeting, endIdx unchanged because it may not end yet
            else: # when a new meeting starts, the current meeting has ended
                avail += 1
                endIdx += 1

        return rooms

    def minMeetingRooms1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, endIdx, n = 0, 0, len(intervals)
        for i in range(n):
            if start[i] < end[endIdx]:
                res += 1
            else:
                endIdx += 1
        return res
