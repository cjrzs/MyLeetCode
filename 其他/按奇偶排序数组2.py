"""
coding: utf8
@time: 2020/11/12 8:23
@author: cjr
@file: 按奇偶排序数组2.py
题目链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii/
"""
from typing import List


class Solution:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        """
        这道题简单的思路，可以直接遍历然后另外开一个数组存结果
        但是也可以原地转换
        :param A:
        :return:
        """
        # 记录奇数位位置
        j = 1
        # 遍历偶数位下标
        for i in range(0, len(A), 2):
            # 如果偶数位下标是奇数
            if A[i] % 2 == 1:
                # 就找到奇数下标的值是偶数的与其交换
                while A[j] % 2 == 0:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A




