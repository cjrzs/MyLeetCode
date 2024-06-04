'''
coding:utf8
@Time : 2020/6/18 23:59
@Author : cjr
@File : 从先序遍历还原二叉树.py
题目链接：https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal/
'''
class TreeNode:
    """
    说实话这题我完全不懂
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        path, pos = list(), 0
        while pos < len(S):
            level = 0
            while S[pos] == '-':
                level += 1
                pos += 1
            value = 0
            while pos < len(S) and S[pos].isdigit():
                value = value * 10 + (ord(S[pos]) - ord('0'))
                pos += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
        return path[0]

