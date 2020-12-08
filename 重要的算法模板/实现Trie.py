"""
coding: utf8
@time: 2020/12/8 15:44
@author: cjr
@file: 实现Trie.py
题目链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree/
"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.END_OF_WORD = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.END_OF_WORD] = self.END_OF_WORD

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.END_OF_WORD in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

