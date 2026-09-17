class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         k=0
#         n=len(intervals)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if (intervals[i][0]<=intervals[j][0]<intervals[i][1]):
#                     k+=1
#         return k