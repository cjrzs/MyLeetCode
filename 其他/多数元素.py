'''
coding:utf8
@Time : 2020/5/24 16:06
@Author : cjr
@File : 多数元素.py
题目链接：https://leetcode-cn.com/problems/majority-element/
'''


class Solution:

    def majorityElement(self, nums: list) -> int:
        new_dict = {}
        for i in nums:
            if i in new_dict:
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        new_list = sorted(new_dict.items(), key=lambda kv: (kv[1], kv[0]))
        return new_list[-1][0]
