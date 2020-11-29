"""
coding: utf8
@time: 2020/11/29 20:33
@author: cjr
@file: 最长有效括号.py
题目链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            # 当前括号如果是左括号，则是0。所以必须是右括号才有意义
            if s[i] == ')':
                # 如果上一个括号是左括号，说明能与当前的右括号组成一对
                if s[i - 1] == '(':
                    # 如果下标超过2 说明有两个以上的括号，否则当前括号与上一个括号组成第一对
                    if i - 2 >= 0:
                        # dp[i - 2]是 当前与当前-1 之前有多少对括号，然后加上当前一对2个括号
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                else:
                    # 如果上一个括号是右括号，则组成 )) 这样的组合。 那我们就要判断((...))这种情况
                    # i - dp[i - 1] - 1 这个位置就是上面那个组合中的第一个括号的位置。
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        # 在上面括号组合的基础上再减去1，就是((...))之前的位置。如果有的话。
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] = dp[i - dp[i - 1] - 2] + 2 + dp[i - 1]
                        else:
                            dp[i] = dp[i - 1] + 2
        return max(dp)





