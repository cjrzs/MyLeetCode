"""
coding: utf8
@time: 2021/2/23 21:59
@author: cjr
@file: 1052. 爱生气的书店老板.py
题目链接：https://leetcode-cn.com/problems/grumpy-bookstore-owner/
"""
from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = 0
        # 先算出来不生气时候的人数
        for i, j in zip(customers, grumpy):
            if j == 0:
                res += i
        # 再算出来[0， X)内使用秘密技巧不生气时候的人数
        cur = 0
        for i in range(X):
            if grumpy[i] == 1:
                cur += customers[i]
        # 然后算出来[X, n)时候使用秘密技巧不生气时候的人数（滑窗）
        sum_ = cur
        for i in range(X, len(grumpy)):
            if grumpy[i] == 1:
                sum_ += customers[i]
            if grumpy[i - X] == 1:
                sum_ -= customers[i - X]
            sum_ = max(sum_, cur)
        return sum_ + res




