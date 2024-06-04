"""
coding: utf8
@time: 2020/11/18 23:10
@author: cjr
@file: 加油站.py
题目链接：https://leetcode-cn.com/problems/gas-station/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        直接暴力法
        :param gas:
        :param cost:
        :return:
        """
        n = len(gas)
        for i in range(n):
            # 设置个单独的变量判断是否可以回到原点
            j = i
            # 当前的油量
            remain = gas[i]
            # 当前油量是否够走到下一个目标
            while remain - cost[j] >= 0:
                # 更新当前油量
                remain += gas[(j + 1) % n] - cost[j]
                # 因为是一个环状所以 % n
                j = (j + 1) % n
                # 如果回到原点则输出该点
                if i == j:
                    return i
        # 没有答案则 -1
        return -1

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        """
        超过99解法，目前仍不得其意
        :param gas:
        :param cost:
        :return:
        """
        remain, start, minn = 0, 0, 0
        n = len(gas)
        for i in range(n):
            remain += gas[i] - cost[i]
            if remain < minn:
                start = i + 1
                minn = remain
        return -1 if remain < 0 else start
