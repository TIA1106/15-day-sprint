import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / float(mid))

            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
