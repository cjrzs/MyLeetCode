"""
coding: utf8
@time: 2021/1/9 15:04
@author: cjr
@file: 买卖股票的最佳时机3.py
题目链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 五种状态
        dp = [[0] * 5 for _ in range(n)]
        # 未有任何操作的状态
        dp[0][0] = 0
        # 第一次交易持股的状态，第一次交易不持股的状态由此转换而来
        dp[0][1] = -prices[0]
        # 第二次交易持股的状态，第二次交易不持股的状态由此转换而来
        dp[0][3] = -prices[0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return max(dp[-1][2], dp[-1][4])



