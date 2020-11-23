"""
coding: utf8
@time: 2020/11/23 13:18
@author: cjr
@file: 用最少数量的箭引爆气球.py
题目链接：https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # count计算移动次数
        count = 1
        # 根据右边界排序
        points.sort(key=lambda x: x[1])
        # 初始化第一个最右边界
        last = points[0][1]
        for i in range(len(points)):
            # 如果左面的数大于最右边界，那么就需要一支新的箭
            # 例如：[1, 6], [2, 8], [7, 12], [10, 16]
            # 我们以第一个元素的右节点为最右边界，当[7, 12]的左节点大于最右边界，
            # 就说明第一支箭无法射到[7, 12], 需要一支新的箭。
            if points[i][0] > last:
                count += 1
                last = points[i][1]
        return count

