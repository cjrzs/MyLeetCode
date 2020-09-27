"""
coding: utf8
@time: 2020/9/27 23:58
@author: cjr
@file: 二叉搜索树的最近公共祖先.py
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_path(root, target):
            path = []
            node = root
            while node.val != target.val:
                path.append(node)
                if node.val > target.val:
                    node = node.left
                else:
                    node = node.right
            path.append(node)
            return path

        path_p = get_path(root, p)
        path_q = get_path(root, q)
        ans = None
        for v, m in zip(path_p, path_q):
            if v == m:
                ans = v
            else:
                break
        return ans


