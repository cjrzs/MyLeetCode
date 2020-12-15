"""
coding: utf8
@time: 2020/12/15 16:04
@author: cjr
@file: 单调递增的数字.py
题目链接：https://leetcode-cn.com/problems/monotone-increasing-digits/
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        从后往前遍历
        :param N:
        :return:
        """
        nums = [int(i) for i in str(N)]
        flag = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i - 1] > nums[i]:
                nums[i - 1] -= 1
                flag = i
        for i in range(flag, len(nums)):
            nums[i] = 9
        return int(''.join([str(i) for i in nums]))



