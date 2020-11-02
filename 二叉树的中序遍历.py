"""
coding: utf8
@time: 2020/11/2 22:24
@author: cjr
@file: 二叉树的中序遍历.py
题目链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        迭代法
        :param root:
        :return:
        """
        res = []
        stack = []
        if not root:
            return None
        # 当栈中有元素或者root不空时候进入循环
        while stack or root:
            # 如果有root，就要向左走，因为要中序遍历是  左-->中-->右
            if root:
                stack.append(root)
                root = root.left
            # 左面节点全部入栈后开始加入结果数组中，然后向右走。
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        递归法
        :param root:
        :return:
        """
        res = []

        def helper(root):
            if not root:
                return None
            helper(root.left)
            res.append(root.left)
            helper(root.right)
        helper(root)
        return res
