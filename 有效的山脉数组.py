"""
coding: utf8
@time: 2020/11/3 22:14
@author: cjr
@file: 有效的山脉数组.py
题目链接：https://leetcode-cn.com/problems/valid-mountain-array/
"""
from typing import List


class Solution:

    @staticmethod
    def validMountainArray(A: List[int]) -> bool:
        """
        双指针找峰顶
        :param A:
        :return:
        """
        left, right = 0, len(A)-1
        while left < right and A[left] < A[left+1]:
            left += 1
        while right > 0 and A[right] < A[right-1]:
            right -= 1
        return 0 < left == right < len(A) - 1

    @staticmethod
    def validMountainArray2(A: List[int]) -> bool:
        """
        先找到峰顶
        :param A:
        :return:
        """
        i = 0
        while i+1 < len(A) and A[i] < A[i+1]:
            i += 1
        if i == len(A)-1 or i == 0:
            return False
        while i+1 < len(A) and A[i] > A[i+1]:
            i += 1
        return i == len(A)-1


