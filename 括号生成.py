"""
coding: utf8
@time: 2020/11/4 23:09
@author: cjr
@file: 括号生成.py
题目链接：https://leetcode-cn.com/problems/generate-parentheses/
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        递归方法
        :param n:
        :return:
        """
        res = []

        def dfs(left, right, s):
            # 结束条件 左右括号都等于n
            if left == n and right == n:
                res.append(s)
                return
            # 只有left小于n时候 才可以放入左括号
            if left < n:
                dfs(left + 1, right, s + '(')
            # right小于left时候才能放入右括号
            if right < left:
                dfs(left, right + 1, s + ')')
        dfs(0, 0, '')
        return res

    def generateParenthesis1(self, n: int) -> List[str]:
        """
        动态规划
        第一对括号一定是‘()’ ，后面的括号只能是在这个括号中间或者右面
        因此有状态转移方程dp[i] = "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
        p + q = n - 1
        参考题解：
        https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/
        :param n:
        :return:
        """
        dp = [[] for _ in range(n+1)]
        dp[0] = ''
        for i in range(1, n+1):
            for p in range(i):
                l1 = dp[p]
                l2 = dp[n - 1 - p]
                for k1 in l1:
                    for k2 in l2:
                        dp[i].append(f'({k1}){k2}')
        return dp[n]
