"""
coding: utf8
@time: 2020/10/28 8:22
@author: cjr
@file: 独一无二的出现次数.py
题目链接：https://leetcode-cn.com/problems/unique-number-of-occurrences/
"""
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        先统计个数，然后去重，看剩下的是否还与原个数一样
        :param arr:
        :return:
        """
        count = dict(Counter(arr))
        val = list(count.values())
        val.sort()
        tmp = list(set(val))
        tmp.sort()
        return tmp == val



