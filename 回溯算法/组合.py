"""
coding: utf8
@time: 2020/11/8 22:47
@author: cjr
@file: 组合.py
题目链接：https://leetcode-cn.com/problems/combinations/
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        直接回溯模板就好了
        :param n:
        :param k:
        :return:
        """
        res = []

        def dfs(index, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(index, n):
                path.append(i)
                dfs(i + 1, path)
                path.pop()
        dfs(0, [])
        return res
