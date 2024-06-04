"""
coding: utf8
@time: 2020/12/3 23:11
@author: cjr
@file: 拼接字符串.py
题目链接：https://leetcode-cn.com/problems/create-maximum-number/
"""
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def pick_max(nums, k):
            remain = len(nums) - k
            stack = []
            for num in nums:
                while stack and remain and stack[-1] < num:
                    stack.pop()
                    remain -= 1
                stack.append(num)
            return stack[: k]

        def merge(A, B):
            res = []
            while A or B:
                # 这里比较首位元素大小，判断列表大小
                bigger = A if A > B else B
                res.append(bigger.pop(0))
            return res

        return max(merge(pick_max(nums1, k), pick_max(nums2, k - i)) for i in range(k + 1) if i <= len(nums1)
                   and k - i <= len(nums2))






