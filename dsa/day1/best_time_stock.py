class Solution(object):
    def maxProfit(self,prices):
        profits = []
        for i in range(1, len(prices)):
            profits.append(prices[i] - prices[i - 1])
        curr= 0
        maxi= 0
        for p in profits:
            curr= max(p, curr+p)
            maxi = max(maxi, curr)

        return maxi

        
