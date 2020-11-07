"""
coding: utf8
@time: 2020/11/7 22:10
@author: cjr
@file: pow.py
题目链接：https://leetcode-cn.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        直接递归
        :param x:
        :param n:
        :return:
        """

        def helper(n):
            # 结束条件n为0时候结果必是1
            if n == 0:
                return 1
            res = helper(n // 2)
            return res * res if n & 2 == 0 else res * res * x

        return helper(n) if n > 0 else 1 / helper(-n)
