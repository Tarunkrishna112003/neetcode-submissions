class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=float('-inf')
        mas=float('-inf')
        for i in nums:
            cur=max(i,cur+i)
            mas=max(mas,cur)
        return mas