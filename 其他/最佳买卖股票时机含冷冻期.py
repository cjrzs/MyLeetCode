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
        """
        动态规划，状态转移方程，看代码
        分三种情况：
        1、dp[i][0] 是当前i持有股票的时候
        2、dp[i][1] 是不持有股票且明天是冷冻期
        3、dp[i][2] 是不持有股票且明天不是冷冻期
        :param prices:
        :return:
        """
        if not prices:
            return 0
        n = len(prices)

        dp = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        print(dp)

        for i in range(1, n-1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        # 最后的结果因为最后一天不会持有股票，如果最后一天持有股票卖不出去肯定亏
        # 所以我们只需要比较其他两种情况即可
        return max(dp[i - 1][1], dp[i - 1][2])

    def maxProfit2(self, prices: List[int]) -> int:
        """
        空间优化
        因为i的结果只与i-1有关，所以我们不必存储i-1以外的结果
        这里我们只借助变量保存i-1的结果
        :param prices:
        :return:
        """
        if not prices:
            return 0

        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            newf0 = max(f0, f2 - prices[i])
            newf1 = f0 + prices[i]
            newf2 = max(f1, f2)
            f0, f1, f2 = newf0, newf1, newf2

        return max(f1, f2)



