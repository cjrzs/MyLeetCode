"""
coding: utf8
@time: 2021/2/28 22:45
@author: cjr
@file: 实现一个魔法字典.py
题目链接：https://leetcode-cn.com/problems/implement-magic-dictionary/submissions/
"""
from typing import List
import collections


class MagicDictionary:
    """
    字典树模板 + BFS
    其中队列中存放的是当前节点和是否修改过的状态（True or False）
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def buildDict(self, dict: List[str]) -> None:
        for word in dict:
            p = self.d
            for c in word + '$':
                if c not in p:
                    p[c] = {}
                p = p[c]
        # print(self.d)

    def search(self, word: str) -> bool:
        word += '$'

        q = collections.deque([(self.d, False)])
        for c in word:
            for _ in range(len(q)):
                # print(word, [(n.keys(), m) for n, m in q])
                node, modified = q.popleft()
                if c in node:
                    q += [(node[c], modified)]
                if not modified:
                    q += [(node[k], True) for k in node if k != c]

        # print(word, q)
        for node, modified in q:
            if node == {} and modified:
                return True
        return False








