'''
coding:utf8
@Time : 2020/6/4 23:11
@Author : cjr
@File : 除自身以外数组的乘积.py
题目链接：https://leetcode-cn.com/problems/product-of-array-except-self/
'''
import typing


class Solution:

    def productExceptSelf(self, nums: typing.List[int]) -> typing.List[int]:
        n = len(nums)
        # 构造左右数组
        left, right, res = [0] * n, [0] * n, [0] * n
        # 因为左右初始化时候左右面都没有元素，前缀乘以后缀直接等于后缀，所以直接初始化前缀为1
        left[0] = 1
        right[n-1] = 1
        # 计算左面数组
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        # 计算右面数组
        for i in reversed(range(n-1)):
            right[i] = nums[i+1] * right[i+1]
        # 计算答案数组
        for i in range(n):
            res[i] = left[i] * right[i]
        return res


