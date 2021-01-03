class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：遍历，如果nums[i],nums[j]都不为0，则 i,j都加一，
        # 若nums[i] == 0,则i不动，j走到第一个不为0的下标，交换。
        # 交换后nums[i] ！= 0，则i,j都加一。
        n = len(nums)
        i = 0
        j = 0
        while j <= n-1:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] != 0:
                i += 1
            j += 1
        return nums