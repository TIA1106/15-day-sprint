class Solution(object):
    def shipWithinDays(self, weights, days):
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            curr=0
            day=1
            for x in weights:
                if x+curr>mid:
                    day=day+1
                    curr=0
                curr=curr+x
            if day<=days:
                high=mid
            else:
                low=mid+1
        return low
