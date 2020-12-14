"""
coding: utf8
@time: 2020/12/14 16:29
@author: cjr
@file: 编辑距离.py
题目链接：https://leetcode-cn.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        # dp[i][j] 表示word1[0: i] 转换到word2[0: j] 需要用到的步数
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 初始化边界
        for i in range(n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(n2 + 1):
            dp[0][i] = dp[0][i + 1] + 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # 状态转移方程： dp[i][j] = dp[i - 1][j - 1] if word1[i] == word2[j]
                # else dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]



