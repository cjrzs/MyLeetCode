'''
coding:utf8
@Time : 2020/7/10 13:44 
@Author : CJR  
@File : 最佳买卖股票时机含冷冻期.py
题目链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        dp = [[-prices[0], 0 ,0]] + [[0] * 3 for _ in range(n - 1)]
        print(dp)

        for i in range(1, n-1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        return max(dp[i - 1][1], dp[i - 1][2])
