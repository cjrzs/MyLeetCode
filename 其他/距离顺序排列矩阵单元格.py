"""
coding: utf8
@time: 2020/11/17 22:30
@author: cjr
@file: 距离顺序排列矩阵单元格.py
题目链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order/
"""
from typing import List
from collections import defaultdict


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """
        直接暴力法，循环之后根据曼哈顿距离排序。
        :param R:
        :param C:
        :param r0:
        :param c0:
        :return:
        """
        res = []
        for i in range(R):
            for j in range(C):
                res.append([i, j])
        res = sorted(res, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return res

    def allCellsDistOrder2(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """
        听说叫桶排序
        :param R:
        :param C:
        :param r0:
        :param c0:
        :return:
        """
        # 确定最大的那个曼哈顿值
        max_path = max(r0, R - r0 - 1) + max(c0, C - c0 - 1)
        # 字典存储桶
        res = defaultdict(list)
        result = []
        # 获取曼哈顿值
        dist = lambda i, j, r0, c0: abs(i - r0) + abs(j - c0)
        # 两次遍历
        for i in range(R):
            for j in range(C):
                res[dist(i, j, r0, c0)].append([i, j])
        print(f'每个元素都放入桶，桶中的元素 {res}')  # {3: [[0, 0]], 2: [[0, 1], [1, 0]], 1: [[0, 2], [1, 1]], 0: [[1, 2]]}

        for i in range(max_path + 1):
            result.extend(res[i])
        print(f'最后输出的结果是： {result}')  # [[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]
        return result


if __name__ == '__main__':
    s = Solution()
    s.allCellsDistOrder2(2, 3, 1, 2)
