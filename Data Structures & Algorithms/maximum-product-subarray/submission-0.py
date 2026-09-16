class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=m=M=nums[0]
        for i in nums[1:]:
            m,M=min(m*i,M*i,i),max(m*i,M*i,i)
            res=max(res,M)
        return res
