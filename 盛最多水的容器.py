"""
coding: utf8
@time: 2020/10/21 21:57
@author: cjr
@file: 盛最多水的容器.py
题目链接：https://leetcode-cn.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针方法
        从两个边界开始求出面积
        每次从小的那条边开始移动
        :param height:
        :return:
        """
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            if height[j] > height[i]:
                res = max(res, (j-i)*height[i])
                i += 1
            else:
                res = max(res, (j-i)*height[j])
                j -= 1
        return res


