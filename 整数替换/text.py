from tihuan import *
"""
给定一个正整数n ，你可以做如下操作：
如果n是偶数，则用n / 2替换n 。
如果n是奇数，则可以用n + 1或n - 1替换n 。
n变为 1 所需的最小替换次数是多少？
8 -> 4 -> 2 -> 1
"""
S = Solution()
n = 8
print(S.integerReplacement(n))
