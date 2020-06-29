'''
coding:utf8
@Time : 2020/6/29 14:54 
@Author : CJR  
@File : 数组中的第K个最大元素.py
题目链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
'''
from typing import List
import random


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        暴力解法：先把数组升序排序，因为是找K个最大的元素
        所以我们从右向左数，即为len(nums)-k
        """
        nums.sort()
        return nums[len(nums) - k]

    def __partition(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left

        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]
        return j

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        size = len(nums)
        left, right = 0, size - 1
        target = size - k

        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[target]
            elif index < target:
                left = index + 1
            else:
                right = index - 1

