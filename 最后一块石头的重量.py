"""
coding: utf8
@time: 2020/12/30 23:11
@author: cjr
@file: 最后一块石头的重量.py
题目链接：https://leetcode-cn.com/problems/last-stone-weight/
"""
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        使用堆，每次弹出来两个，计算他俩的差值之后，把差值放进去
        最后堆里只剩下一个就是最后一块石头的重量了，如果没有返回0
        :param stones:
        :return:
        """
        new = [-item for item in stones]
        heapq.heapify(new)
        while len(new) > 1:
            two, one = heapq.heappop(new), heapq.heappop(new)
            heapq.heappush(new, abs(two - one))
        return -heapq.heappop(new) if new else 0


