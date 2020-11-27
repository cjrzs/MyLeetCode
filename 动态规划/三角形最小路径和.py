"""
coding: utf8
@time: 2020/11/27 15:41
@author: cjr
@file: 三角形最小路径和.py
题目链接：https://leetcode-cn.com/problems/triangle/
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        自下向上的计算，取出下一层最小的加上当前的。
        :param triangle:
        :return:
        """
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]


