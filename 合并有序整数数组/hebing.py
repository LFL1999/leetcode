class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2      # 将nums2合并到nums1中
        nums1.sort()
        return nums1
