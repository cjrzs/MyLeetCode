"""
coding: utf8
@time: 2020/12/29 23:24
@author: cjr
@file: 买卖股票的最佳时机1.py
题目链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_ 当前最小的价格， max_ 当前最大的收入
        min_ = float('inf')
        max_ = 0
        for price in prices:
            # 也有点动态规划的思想。
            # 最大的收入就是用当前的股票价格-目前为止的最小股票价格和上一个最大收入比较
            # 当前最小的股票价格就是当前的股票价格和上一个最小股票价格比较
            max_ = max(price - min_, max_)
            min_ = min(min_, price)
        return max_



