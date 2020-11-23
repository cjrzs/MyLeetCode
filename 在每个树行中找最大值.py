"""
coding: utf8
@time: 2020/11/22 17:35
@author: cjr
@file: 在每个树行中找最大值.py
题目链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            child = []
            node = []
            for item in q:
                child.append(item.val)
                if item.left:
                    node.append(item.left)
                if item.right:
                    node.append(item.right)
            res.append(max(child))
            q = node
        return res


