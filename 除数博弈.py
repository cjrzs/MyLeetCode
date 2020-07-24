"""
coding:utf8
@Time : 2020/7/24 12:27 
@Author : CJR  
@File : 除数博弈.py
题目链接：https://leetcode-cn.com/problems/divisor-game/
"""
class Solution:

    def divisorGame(self, N: int) -> bool:
        """
        找到规律后可以发现，
        当N为偶数时候是T，奇数时候是F
        时/空 复杂度： 全是常量级 O(1)
        :param N:
        :return:
        """
        return not (N % 2)

    def divisorGame2(self, N: int) -> bool:
        """
        动态规划
        时/空 复杂度： O(N), O(N)
        :param N:
        :return:
        """
        dp = [0 for i in range(N + 1)]
        dp[1] = 0
        if N <= 1:
            return False
        else:
            dp[2] = 1
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数且dp[i-j]为假（0）的话，则代表当前为真（1）
                    if i % j == 0 and dp[i - j] == 0:
                        dp[i] = 1
                        break
        return dp[N] == 1


