"""
coding: utf8
@time: 2020/12/20 22:25
@author: cjr
@file: 重新格式化电话号码.py
题目链接：https://leetcode-cn.com/problems/reformat-phone-number/
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        if len(number) <= 3:
            return number
        res = []
        new_list = []
        for ch in number:
            if ch != ' ' and ch != '-':
                if len(new_list) < 3:
                    new_list.append(ch)
                else:
                    res.append(''.join(new_list))
                    new_list.clear()
                    new_list.append(ch)
        else:
            res.append(''.join(new_list))

        if len(res[-1]) == 1:
            tmp = res[-2] + res[-1]
            # print(tmp)
            res = res[:-2]
            res.append(tmp[:2])
            res.append(tmp[2:])

        return '-'.join(res)



