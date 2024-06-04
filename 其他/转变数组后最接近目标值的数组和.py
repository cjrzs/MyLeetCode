'''
coding:utf8
@Time : 2020/6/14 19:22
@Author : cjr
@File : 转变数组后最接近目标值的数组和.py
https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/
'''
import typing


class Solution:
    def findBestValue(self, arr: typing.List[int], target: int) -> int:
        n = len(arr)
        summ = sum(arr)
        if summ <= target:
            return max(arr)

        val = target // n
        summ, res = val * n, 0
        while summ < target:
            res = summ
            summ = 0
            for i in range(n):
                summ += arr[i] if val > arr[i] else val
            val += 1
        return val - 2 if abs(target - summ) >= abs(target - res) else val - 1





