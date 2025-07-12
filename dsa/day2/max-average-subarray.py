class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_avg = window_sum
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_avg = max(max_avg, window_sum)
        return float(max_avg) / k
