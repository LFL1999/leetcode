class Solution:
    def isPalindrome(self, x):
        return (str(x) + str(x))[::1] ==  (str(x) + str(x))[::-1]