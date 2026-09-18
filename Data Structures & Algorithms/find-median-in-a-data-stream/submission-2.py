import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # Inserts 'num' into 'self.nums' while keeping it sorted
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        mid = n // 2
        
        # If even number of elements, average the middle two
        if n % 2 == 0:
            return (self.nums[mid - 1] + self.nums[mid]) / 2.0
        # If odd number of elements, return the middle element
        else:
            return float(self.nums[mid])