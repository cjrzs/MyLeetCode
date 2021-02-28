"""
coding: utf8
@time: 2021/2/28 23:04
@author: cjr
@file: 最大交换.py
题目链接：https://leetcode-cn.com/problems/maximum-swap/
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        s, n = [i for i in str(num)], len(str(num))
        for i in range(0, n - 1):
            # 找到第一个严格递增的位置，如果全部递减则不需要交换本身就是最大的
            if s[i] < s[i + 1]:
                k = i + 1
                # 找到这个位置后面最大的，如果最大的相同则往后取。
                # 因为后面的位置越靠后交换后就越大,最后得到k
                for j in range(k, n):
                    if s[j] >= s[k]:
                        k = j
                # 从最高位开始，如果有s[i] < s[k]。交换即可。
                for j in range(n):
                    if s[j] < s[k]:
                        s[j], s[k] = s[k], s[j]
                        return int(''.join(s))
        return num


