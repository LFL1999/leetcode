class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        nums1.sort()
        nums2.sort()
        c1, c2 = 0, 0
        result = []
        while c1 < len(nums1) and c2 < len(nums2):
            if nums1[c1] == nums2[c2]:
                result.append(nums1[c1])
                c1 += 1
                c2 += 1
            elif nums1[c1] > nums2[c2]:
                c2 += 1
            elif nums1[c1] < nums2[c2]:
                c1 += 1
        return result