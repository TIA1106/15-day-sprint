class Solution(object):
    def maxArea(self, height):
        x = 0
        y = len(height) - 1
        Area = 0
        while x < y:
            curr = (y - x) * min(height[x], height[y])
            if curr > Area:
                Area = curr

            if height[x] < height[y]:
                x += 1
            else:
                y -= 1

        return Area
