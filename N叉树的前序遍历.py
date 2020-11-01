"""
coding: utf8
@time: 2020/11/1 14:30
@author: cjr
@file: N叉树的前序遍历.py
题目链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
"""
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        简单的递归遍历
        :param root:
        :return:
        """
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res

    def preorder1(self, root: 'Node') -> List[int]:
        """
        使用迭代的方式，自己维护一个栈
        :param root:
        :return:
        """
        stack = [root, ]
        res = []
        if not root:
            return []
        while stack:
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
        return res


