"""
coding:utf8
@Time : : 2020/10/14 18:07
@Author : CJR
@File : 查找常用字符.py
题目链接：https://leetcode-cn.com/problems/find-common-characters/
"""
from collections import Counter
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # 使用python的内置库Counter，两两比较得出共有的元素
        res = Counter(A[0])
        for i in range(1, len(A)):
            res = res & Counter(A[i])
        return list(res.elements())


