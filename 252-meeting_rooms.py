# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals = sorted(intervals, key=lambda d: d.start)
        i = 0
        while i < len(intervals)-1:
            if intervals[i+1].start < intervals[i].end:
                return False
            i += 1
        return True
            
