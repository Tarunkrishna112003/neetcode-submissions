"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
        # n=len(intervals)

        # if n==0:return True

        # leftind=intervals[0].start
        # rightind=intervals[0].end

        # for i in range(1,n):
        #     if leftind<=intervals[i].start<rightind:
        #         return False
        #     leftind=intervals[i].start
        #     rightind=intervals[i].end
        # return True

