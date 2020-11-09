"""
coding: utf8
@time: 2020/11/9 21:28
@author: cjr
@file: 最接近原点的 K 个点.py
题目链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/
"""
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        本题其实就是一个排序
        算出距离然后各种算法排序
        这里就不麻烦了 直接用sort排序了
        :param points:
        :param K:
        :return:
        """
        points.sort(lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]
