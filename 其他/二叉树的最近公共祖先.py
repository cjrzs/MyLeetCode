"""
coding: utf8
@time: 2020/11/8 18:17
@author: cjr
@file: 二叉树的最近公共祖先.py
题目链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        这道题好晦涩
        可以先理解为找祖先，而不是找公共祖先。
        函数功能有以下三点：
        1、如果 p 和 q 都存在，则返回它们的公共祖先；
        2、如果只存在一个，则返回存在的一个；
        3、如果 p 和 q 都不存在，则返回NULL
        :param root:
        :param p:
        :param q:
        :return:
        """
        #  因为题目中有说明节点本身也可以是最终的公共祖先，所以如果节点本身等于root那就代表找到了。
        if not root or root.val == p.val or root.val == q.val:
            return root
        # 向下进行遍历
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 如果left或者right有一个为空，则代表这个分支必没有公共祖先，那就要返回另一个分支
        if not left:
            return right
        if not right:
            return left
        return root


