"""
coding: utf8
@time: 2021/3/3 22:27
@author: cjr
@file: 比特位计数.py
题目链接：https://leetcode-cn.com/problems/counting-bits/
"""
from typing import List


class Solution:
    """
    这道题其实就是考察lowbit的裸题。
    lowbit(x)总是返回x二进制最后一个1的位置。例如：
    lowbit(10) 其中10的二进制是1010，则lowbit(10) ==> 10。
    如果lowbit(x) 其中x的二进制是101000，则lowbit(x) ==> 1000
    lowbit(x) 实现的方式超级简单就是 x & -x
    等同于 x & (-x + 1)， 其中-x表示x的补码。
    """
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            cur = 0
            count = 0
            # 这个循环也非常简单就只是每次循环减去最后一个1，
            # 一直减到0，每减一次计数 +1。
            while cur:
                count += 1
                cur -= self.lowbit(cur)
            res.append(count)
        return res

    def lowbit(self, x):
        return x & -x




