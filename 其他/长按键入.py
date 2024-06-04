"""
coding:utf8
@Time : : 2020/10/21 11:56
@Author : CJR
@File : 长按键入.py
题目链接:https://leetcode-cn.com/problems/long-pressed-name/
"""
import collections


class Solution:
    @staticmethod
    def isLongPressedName(name: str, typed: str) -> bool:
        """
        设置两个指针一个负责name,一个负责typed，
        typed总共两个功能如果和name相等则两个指针同时后移
        如果与name相等，但是与前面的元素相等则是长按键j自己后移
        如果以上两种情况都不满足则是False，如果遍历完typed则判断i是否到底。
        :param name:
        :param typed:
        :return:
        """
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j < 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


if __name__ == '__main__':
    print(Solution.isLongPressedName("ssaeed", "ssaaedd"))


