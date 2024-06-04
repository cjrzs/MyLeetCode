"""
coding: utf8
@time: 2020/11/10 0:16
@author: cjr
@file: 单词接龙.py
题目链接：https://leetcode-cn.com/problems/word-ladder/
"""
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 and endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        # BFS用队列
        queue = deque()
        queue.append(beginWord)
        # 记录已经访问过的元素
        visited = set(beginWord)
        word_len = len(beginWord)
        # 记录经过节点数量，因为有个起始节点所以为1
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()
                # wordlist 是单词字母组成的列表
                word_list = list(word)
                for j in range(word_len):
                    # origin_char是单词的字母
                    origin_char = word_list[j]
                    for k in range(26):
                        # 把26个字母挨个赋值给当前的单词元素
                        word_list[j] = chr(ord('a') + k)
                        # 用新字母去组成字符串
                        next_word = ''.join(word_list)
                        # 判断新组成的字符串在不在单词列表
                        # 在的话有两种情况
                        # 1、与endword一样就找到了，结果加一（step+1）
                        # 2、没有遍历过，就是不在visited，放到visited，然后把这个单词放到queue。
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                visited.add(next_word)
                                # 跟着这个单词往下走
                                queue.append(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0