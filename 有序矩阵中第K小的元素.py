'''
coding:utf8
@Time : 2020/7/2 16:06 
@Author : CJR  
@File : 有序矩阵中第K小的元素.py
本题链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        将二维矩阵变成一维矩阵之后，从小到大排序好
        取第k-1即可。
        :param matrix:
        :param k:
        :return:
        """
        new_list = []
        for i in matrix:
            for j in i:
                new_list.append(j)

        print(new_list)
        new_list.sort()
        return new_list[k-1]

