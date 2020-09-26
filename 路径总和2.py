"""
coding: utf8
@time: 2020/9/26 17:49
@author: cjr
@file: 路径总和2.py
题目链接：https://leetcode-cn.com/problems/path-sum-ii/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        """
        类似回溯的方法，
        用给的目标值减去每一个节点
        当没有左右节点（也就是叶子节点）和目标值变成0时候，把这个数组放入结果中。
        :param root:
        :param sum:
        :return:
        """
        res = []
        track = []

        def dfs(root, total):
            if not root:
                return
            track.append(root.val)
            total -= root.val
            if not root.left and not root.right and total == 0:
                res.append(track[:])
            dfs(root.left, total)
            dfs(root.right, total)
            track.pop()
        dfs(root, sum)
        return res


