"""
coding:utf8
@Time : 2020/7/23 13:32 
@Author : CJR  
@File : 最小路径和.py
题目链接：https://leetcode-cn.com/problems/minimum-path-sum/
"""
from typing import List


class Solution:
    """
    动态规划
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m是横坐标，n是纵坐标
        n, m = len(grid), len(grid[0])
        # 初始化dp二维数组
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        # 设定边界数值
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        # 状态转移方程：dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


