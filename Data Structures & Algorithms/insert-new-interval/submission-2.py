class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        n = len(intervals)
        leftind = newInterval[0]
        rightind = newInterval[1]
        leftlimit = 0
        rightlimit = n

        # Find where left boundary begins
        for i in range(n):
            if intervals[i][1] < leftind:
                leftlimit = i + 1
            elif intervals[i][0] <= leftind <= intervals[i][1]:
                leftind = intervals[i][0]
                leftlimit = i
                break

        # Find where right boundary ends
        for i in range(n):
            if intervals[i][0] <= rightind <= intervals[i][1]:
                rightind = intervals[i][1]
                rightlimit = i + 1
                break
            elif intervals[i][0] > rightind:
                rightlimit = i
                break

        # Fixed: Wrap [leftind, rightind] in an extra list []
        return intervals[:leftlimit] + [[leftind, rightind]] + intervals[rightlimit:]