from shan import *
"""
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
说明: 输入可能包含了除 ( 和 ) 以外的字符。
"""
S = Solution()
n = "()())()"
print(S.removeInvalidParentheses(n))