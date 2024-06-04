"""
coding: utf8
@time: 2021/2/28 22:58
@author: cjr
@file: 二叉树中的第二小节点.py
题目链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
"""
from 不同的二叉搜索树2 import TreeNode


class Solution:
    """
    在这题里运用一个小技巧，
    先设置d1和d2两个最小节点和第二小的节点
    那么当前节点x如果小于d1，最小节点d1更新为x，原d1更新为新的d2
    如果当前节点x大于d1小于d2，x就变成了新的d2
    然后递归左右节点即可。
    """
    def __init__(self):
        self.d1 = float('inf')
        self.d2 = float('inf')

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.helper(root)
        if self.d2 == float('inf'):
            self.d2 = -1
        return self.d2

    def helper(self, root):
        if not root:
            return
        x = root.val
        if x < self.d1:
            self.d2, self.d1 = self.d1, x
        elif self.d1 < x < self.d2:
            self.d2 = x
        self.helper(root.left)
        self.helper(root.right)



