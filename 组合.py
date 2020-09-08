"""
coding:utf8
@Time : 2020/9/8 10:48 
@Author : CJR  
@File : 组合.py
题目链接：https://leetcode-cn.com/problems/combinations/
"""
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(remain, unfinshed, track):
            if unfinshed == 0:
                return res.append(track[:])
            tmp_length = len(remain)
            for i in range(tmp_length):
                if unfinshed <= tmp_length - i + 1:
                    dfs(remain[i + 1:], unfinshed - 1, track + [remain[i]])
                else:
                    break
        if n < k and n <= 0 and k <= 0:
            return []
        dfs([i for i in range(1, n + 1)], k, [])
        return res

