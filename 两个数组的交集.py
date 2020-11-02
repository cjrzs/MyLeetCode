"""
coding: utf8
@time: 2020/11/2 21:11
@author: cjr
@file: 两个数组的交集.py
题目链接：https://leetcode-cn.com/problems/intersection-of-two-arrays/
"""
from typing import List


class Solution:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        暴力法
        :param nums1:
        :param nums2:
        :return:
        """
        res = []
        for num in nums1:
            if num in nums2 and num not in res:
                res.append(num)
        return res

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        还是暴力法 只是用了set去重
        :param nums1:
        :param nums2:
        :return:
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [x for x in nums1 if x in nums2]

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        用了两个指针，速度快了不少
        :param nums1:
        :param nums2:
        :return:
        """
        res = set()
        nums1.sort()
        nums2.sort()
        first, second = 0, 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                res.add(nums1[first])
                first += 1
                second += 1
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                first += 1
        return list(res)