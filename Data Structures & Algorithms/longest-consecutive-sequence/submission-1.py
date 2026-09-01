class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        k=[1]*len(nums)
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]+1 ):
                k[i]=k[i-1]+1
            elif nums[i]==nums[i-1]:
                k[i]=k[i-1]
        return max(k)

