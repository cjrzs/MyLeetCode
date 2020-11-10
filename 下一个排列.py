"""
coding: utf8
@time: 2020/11/10 23:57
@author: cjr
@file: 下一个排列.py
题目链接：https://leetcode-cn.com/problems/next-permutation/
"""
from typing import List


class Solution:
    """
    经典算法，画出过程更易理解
    从后往前遍历，找到第一个非降序元素，例如：1,2,3,8,4,9,5,3,1 我们找到第一个非降序元素就是4
    然后再找到第一个比4大的元素的位置，将该元素与4交换。该例子中就是5，交换后得到1,2,3,8,5,9,4,3,1
    可以看到5后面的所有元素依旧是有序的，从大到小排列好的，那要求最小，就要将后面的元素原地倒序。
    使用双指针倒序即可。
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



