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

    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        """
        二分法
        完全利用有序矩阵的两个特性
        :param matrix:
        :param k:
        :return:
        """
        n = len(matrix)

        def check(mid):
            # 这是左左下角
            i, j = n - 1, 0
            num = 0
            # 计算出左半区的元素（小于mid）个数
            # 如果小于就把该列的不大于mid的数量（i+1）累加到答案，并且向右移动（j+1），因为矩阵特性右面大于左面
            # 如果大于那就向上移动（因为矩阵特性，上面的数字小于下面的）
            while j < n and i >= 0:
                # 以左下角为起点
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            # 最后用左面数字个数与k比较，因为本题目要求找出的是第k小的元素
            return num >= k
        # 以左上角，右下角两个最大，最小值为起点，做二分法。
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            mid = (left + right)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


