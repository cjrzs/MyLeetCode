'''
coding:utf8
@Time : 2020/4/27 23:33
@Author : cjr
@File : 买卖股票的最佳时机.py
本题链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
'''


class Solution:
    def maxProfit(self, prices: list) -> int:
        ans = 0
        stack = []
        for i in range(len(prices)):
            if not stack or prices[i] < prices[stack[-1]]:
                stack.append(i)
        for i in range(len(prices) - 1, -1, -1):
            print(i)
            if i == stack[-1]:
                stack.pop()
                continue
            if prices[i] > prices[stack[-1]]:
                ans = max(ans, prices[i] - prices[stack[-1]])
        return ans


if __name__ == '__main__':
    com = Solution()
    res = com.maxProfit([7,1,5,3,6,4])
    print(res)
