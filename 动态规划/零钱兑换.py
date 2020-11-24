"""
coding: utf8
@time: 2020/11/24 12:12
@author: cjr
@file: 零钱兑换.py
题目链接：https://leetcode-cn.com/problems/coin-change/
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化的dp数组是存放的组成0-amount面值最少个数。
        # 其中初始化存放的是不可能达到的总金额。
        dp = [amount + 1] * (amount + 1)
        # 其中最初的位置dp[0] = 0也是成立的，也属于最优子结构
        dp[0] = 0
        # 然后要遍历1-amount，找他们的最少个数
        for i in range(1, amount + 1):
            # 硬币的面值
            for coin in coins:
                # 如果当前的总金额大于等于当前的单个面值，上一次结果不为不可能面值时候才可以进入状态庄毅方程
                # 状态转移方程： dp[i] = min(dp[i], dp[i - coin] + 1)
                if i >= coin and dp[i - coin] != (amount + 1):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        # 根据题目要求 如果最后的结果是不可能结果则返回-1。
        return -1 if dp[amount] == amount + 1 else dp[amount]

