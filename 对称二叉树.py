'''
coding:utf8
@Time : 2020/4/1 1:15
@Author : cjr
@File : 对称二叉树.py
题目链接：https://leetcode-cn.com/problems/symmetric-tree/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    本题题解：
    首先明确终止条件
    当左右节点都为空，自然相等返回true
    当左右节点有一个为空，另一个还没有空，则不等
    当全部遍历完，
    左节点的左节点和右节点的右节点相等
    左节点的右节点和右节点的左节点相等
    判断改二叉树对称
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def new_tree(left, right):
            if not left or not right:
                return True
            if not left and not right:
                return False
            if left.val != right.val:
                return False
            return new_tree(left.left, right.right) and new_tree(left.right, right.left)
        return new_tree(root.left, root.right)



