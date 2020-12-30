"""
coding: utf8
@time: 2020/12/30 23:56
@author: cjr
@file: 买卖股票的最佳时机2.py
题目链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]

