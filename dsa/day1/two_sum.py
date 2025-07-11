#leetcode solution
class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            h=target-nums[x]
            for j in range(x + 1, len(nums)):
                if nums[j] == h:
                    return [x, j]
