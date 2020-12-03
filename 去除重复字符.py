"""
coding: utf8
@time: 2020/12/2 22:31
@author: cjr
@file: 去除重复字符.py
题目链接：https://leetcode-cn.com/problems/remove-duplicate-letters/
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        本题解法：
        1、建立一个字典。其中 key 为 字符 c，value 为其出现的剩余次数。
        2、从左往右遍历字符串，每次遍历到一个字符，其剩余出现次数 - 1.
        3、对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃（也可以选择不丢弃），否则不可以丢弃。
        4、如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。
        :param s:
        :return:
        """
        # 算出每个字符出现的次数，要把每个字符这个次数归一
        counts = Counter(s)
        # 生成一个栈，保存字符，并且生成一个hash判断字符是否有被遍历过，降低复杂度
        stack, visit = [], set()
        for char in s:
            if char not in visit:
                # 题解中提到的丢弃元素，条件3和4
                while stack and stack[-1] > char and counts[stack[-1]] > 0:
                    visit.discard(stack.pop())
                stack.append(char)
                visit.add(char)
            counts[char] -= 1
        return ''.join(stack)


