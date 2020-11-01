"""
coding: utf8
@time: 2020/11/1 21:24
@author: cjr
@file: 字母异位词分组.py
题目链接：https://leetcode-cn.com/problems/group-anagrams/
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        排序
        使用字典的get方法载入排序后相同元素。
        :param strs:
        :return:
        """
        dic = {}
        for ss in strs:
            key = tuple(sorted(ss))
            dic[key] = dic.get(key, []) + [ss]
        return list(dic.values())
