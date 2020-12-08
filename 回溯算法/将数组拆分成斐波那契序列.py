"""
coding: utf8
@time: 2020/12/8 12:18
@author: cjr
@file: 将数组拆分成斐波那契序列.py
题目链接：https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/
"""
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []

        # dfs回溯
        def dfs(start):
            # 如果当前下标和S长度一样表示遍历到了最后
            if start == len(S):
                # 我们看res里面的是否大于三个。如果大于三个说明是找到了Fibonacci的。
                return len(res) >= 3
            curr = 0

            for i in range(start, len(S)):
                # 从字符串计算数字的值，因为没次循环一个就要进位一次，所以要 *10
                curr = curr * 10 + ord(S[i]) - ord('0')
                # 判断0是否合法，如果0不是第一个数，则第一个数不可以是0
                if i > start and S[start] == '0':
                    break
                # 判断curr是否超出整数范围
                if curr > 2 ** 31 - 1:
                    break
                # 如果res数量小于2 就可以把数放进去，如果不小于2 就可以判断是否符合斐波那契数列标准了
                if len(res) < 2 or curr == res[-2] + res[-1]:
                    # 符合条件进行回溯
                    res.append(curr)
                    if dfs(i + 1):
                        return True
                    res.pop()
                # 如果说res元素数量超过2 并且当前值直接大于前连个值，那么说明该序列已经不可拆分了。
                elif len(res) > 2 and curr > res[-2] + res[-1]:
                    break
            return False
        dfs(0)
        return res


