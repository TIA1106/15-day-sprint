class Solution(object):
    def search(self, nums, target):
        for x in range(len(nums)):
            if nums[x]==target:
                return x
        return -1
        
