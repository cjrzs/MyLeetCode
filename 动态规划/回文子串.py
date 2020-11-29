"""
coding: utf8
@time: 2020/11/29 19:24
@author: cjr
@file: 回文子串.py
题目链接：https://leetcode-cn.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(i):
                # 单个字符时候必定是回文串
                if i == j:
                    dp[i][j] = True
                    count += 1
                # 两个字符时候，如果两个字符相等也是回文串
                elif i - j == 1 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                # 两个以上字符时候
                elif i - j > 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1
        return count




