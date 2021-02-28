"""
coding: utf8
@time: 2021/2/28 22:50
@author: cjr
@file: 灯泡开关2.py
题目链接：https://leetcode-cn.com/problems/bulb-switcher-ii/
"""


class Solution:
    """
    仔细分析，其实本题状态有限
    m = 0 只有一种状态
    m = 1 可能有1， 2， 3， 4 各执行一遍四种状态
    m = 2 可能有0， 1， 2， 3， 14， 24，34七种状态，
    因为先1，再2，其实和执行一次3状态一样，先1再3其实和执行一次2状态一样，最后先2再3就相当于执行一次1
    m >= 3 可能有0， 1， 2， 3，4， 14， 24，34八种状态。
    """
    def flipLights(self, n: int, m: int) -> int:
        # 当n小于等于2时候情况会有不同，所以需要特判。
        if n == 0:
            return 1
        if n == 1:
            if m == 0:
                return 1
            return 2
        if n == 2:
            if m == 0:
                return 1
            if m == 1:
                return 3
            return 4
        # 枚举上面的分析即可
        if m == 0:
            return 1
        if m == 1:
            return 4
        if m == 2:
            return 7
        return 8


