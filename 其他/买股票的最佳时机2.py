'''
coding:utf8
@Time : 2020/5/6 21:30
@Author : cjr
@File : 买股票的最佳时机2.py
题目链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
'''


class Solution:
    """
    题解：
    当连续上涨的时候当天和前一天的差价全部相加就是交易总额
    当不上涨时候当天和前一天的差价小于等于0
    只需要把正数的差价加起来就是赚的总和
    ps:除了这种办法还可以用暴力法，将所有的可能赚到的钱全部算出来，取最大值
    """
    def maxProfit(self, prices: list[int]) -> int:
        # 初始的差价
        tmp = 0
        # 要用当天的股价减去前一天的股价,所以从下标1开始遍历
        for i in range(1, len(prices)):
            tmp2 = prices[i] - prices[i-1]
            if tmp2 > 0:
                tmp += tmp2
        return tmp



