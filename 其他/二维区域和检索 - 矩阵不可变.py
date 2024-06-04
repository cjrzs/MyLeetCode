"""
coding: utf8
@time: 2021/3/3 0:44
@author: cjr
@file: 二维区域和检索 - 矩阵不可变.py
题目链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable/
"""
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return

        n, m = len(matrix), len(matrix[0] if matrix[0] else 0)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][0] = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                f[i + 1][j + 1] = f[i][j + 1] + f[i + 1][j] + matrix[i][j] - f[i][j]
        self.f = f
        # print(f)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        f = self.f
        return f[row2 + 1][col2 + 1] - f[row1][col2 + 1] - f[row2 + 1][col1] + f[row1][col1]



