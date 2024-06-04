"""
coding: utf8
@time: 2020/10/29 16:59
@author: cjr
@file: 求根到叶子节点数字之和.py
题目链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        递归的方式
        :param root:
        :return:
        """
        def helper(root, i):
            # root空值时候的特殊处理。直接返回。
            if not root:
                return 0
            # res： 计算相加后的值
            res = i * 10 + root.val
            # 递归的结束条件 没有左右节点
            if not root.left and not root.right:
                return res
            # 左右节点开始递归
            return helper(root.left, res) + helper(root.right, res)

        return helper(root, 0)
