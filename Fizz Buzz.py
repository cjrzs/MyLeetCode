"""
coding: utf8
@time: 2020/10/29 17:54
@author: cjr
@file: Fizz Buzz.py
题目链接：https://leetcode-cn.com/problems/fizz-buzz/
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append(f'FizzBuzz')
            elif i % 3 == 0:
                res.append(f'Fizz')
            elif i % 5 == 0:
                res.append(f'Buzz')
            else:
                res.append(f'{i}')
        return res

