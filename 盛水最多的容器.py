'''
coding:utf8
@Time : 2020/5/6 22:33
@Author : cjr
@File : 盛水最多的容器.py
题目链接：https://leetcode-cn.com/problems/container-with-most-water/
'''


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        暴力法：
        双重循环 直接求出所有可能的容量，取最大值，但是如果数组太大运行时间太长
        :param height:
        :return:
        """
        ls_x = len(height)
        res = 0
        for x in range(0, ls_x):
            for m in range(x+1, ls_x):
                tmp = min(height[m], height[x]) * (m-x)
                res = max(tmp, res)
        return res




