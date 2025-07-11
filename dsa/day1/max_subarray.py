class Solution(object):
    def maxSubArray(self, nums):
        curr=float('-inf')
        maxi=float('-inf')
        for x in nums:
            curr=max(x,(x+curr))
            maxi=max(curr,maxi)
        return(maxi)
        
