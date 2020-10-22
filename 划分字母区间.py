"""
coding:utf8
@Time : : 2020/10/22 11:15
@Author : CJR
@File : 划分字母区间.py
题目链接：https://leetcode-cn.com/problems/partition-labels/
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        count_s = {ch: idx for idx, ch in enumerate(S)}
        tmp, res, last = {}, [], 0
        for idx, ch in enumerate(S):
            tmp[ch] = idx
            if count_s[ch] == idx:
                tmp.pop(ch)
            if not tmp:
                res.append(idx - last + 1)
                last = idx + 1
        return res
