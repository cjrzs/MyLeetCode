"""
coding: utf8
@time: 2020/11/21 23:30
@author: cjr
@file: 二叉树的层序遍历.py
题目链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        BFS直接套模板
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            node = []
            child = []
            for item in queue:
                child.append(item.val)
                if root.left:
                    node.append(root.left)
                if root.right:
                    node.append(root.right)
            res.append(child)
            queue = node
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        递归DFS方法，通过记录下深度，来把所有节点放在相应的深度列表中
        :param root:
        :return:
        """
        res = []

        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)
        dfs(root, 0)
        return res




