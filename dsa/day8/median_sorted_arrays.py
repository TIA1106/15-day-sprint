class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        if n % 2 != 0:
            mid = n // 2
            return nums3[mid]
        else:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (nums3[mid1] + nums3[mid2]) / 2.0
