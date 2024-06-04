'''
coding:utf8
@Time : 2020/6/28 22:31
@Author : cjr
@File : 长度最小的子数组.py
题目链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/
'''
import typing


class Solution:
    def minSubArrayLen(self, s: int, nums: typing.List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0

        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        if ans == n + 1:
            return 0
        else:
            return ans


