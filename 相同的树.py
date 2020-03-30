'''
coding:utf8
@Time : 2020/3/22 0:40
@Author : cjr
@File : 相同的树.py
题目链接：https://leetcode-cn.com/problems/same-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题解思路:利用递归，暴力思路
    如果q，p全空，那么自然完全相等返回True
    如果有一个空，那么返回False
    递归判断下一个节点
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(q.right, q.right)

