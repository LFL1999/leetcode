class Solution(object):
    def missingNumber(self, nums):
        le = len(nums)
        for i in range(le+1):
            if i not in nums:
                return i
        return False