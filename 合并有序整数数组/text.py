from hebing import *
"""
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
说明：
    初始化nums1 和 nums2 的元素数量分别为m 和 n 。
    你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。
"""
S = Solution()
num1 = [1, 2, 3]
m = 3
num2 = [2, 4, 5]
n = 3
print(S.merge(num1, m, num2, n))