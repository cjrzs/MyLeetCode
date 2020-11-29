"""
coding: utf8
@time: 2020/11/29 18:58
@author: cjr
@file: 最大正方形.py
题目链接：https://leetcode-cn.com/problems/maximal-square/
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0] * col for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j])
        return res * res

