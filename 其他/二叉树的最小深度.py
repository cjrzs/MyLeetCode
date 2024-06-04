'''
coding:utf8
@Time : 2020/4/16 23:28
@Author : cjr
@File : 二叉树的最小深度.py
本题链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if root == 0:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0:
            return max(left, right) + 1
        return min(left, right)




