"""
coding: utf8
@time: 2020/11/22 17:09
@author: cjr
@file: 最小基因变化.py
https://leetcode-cn.com/problems/minimum-genetic-mutation/
"""
from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        set_bank = set(bank)
        count = 0
        visit = set()
        if start in set_bank:
            set_bank.remove(start)
        queue = deque()
        queue.append(start)
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                word_list = list(word)
                for i in range(len(word_list)):
                    flag = word_list[i]
                    for char in ['A', 'C', 'G', 'T']:
                        word_list[i] = char
                        new_word = ''.join(word_list)
                        if new_word in set_bank:
                            if new_word == end:
                                count += 1
                                return count
                            if new_word not in visit:
                                queue.append(new_word)
                                visit.add(new_word)
                    word_list[i] = flag
            count += 1
        return -1













