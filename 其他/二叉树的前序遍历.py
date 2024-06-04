"""
coding: utf8
@time: 2020/11/1 21:42
@author: cjr
@file: 二叉树的前序遍历.py
题目链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/submissions/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root):
            if not root:
                return res
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        res = []
        helper(root)
        return res