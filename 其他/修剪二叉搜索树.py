"""
coding: utf8
@time: 2021/2/28 23:02
@author: cjr
@file: 修剪二叉搜索树.py
题目链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    唔 这题不甚明白 我对递归和树的问题太弱了
    """
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


