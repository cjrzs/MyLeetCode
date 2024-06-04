'''
coding:utf8
@Time : 2020/4/14 23:31
@Author : cjr
@File : 平衡二叉树.py
题目链接：https://leetcode-cn.com/problems/balanced-binary-tree/
'''

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题目解析：其实这里对于新手最难理解就是root.left(root.right)指的是什么
    他其实不是指该点的值，而是指该点在二叉树中的位置。
    理解上面一点之后其实这道题就非常容易了。算出来每个节点上最大的位置加一即可表示该点真实的位置
    因为是从0开始计算的所以要加一，比如说第0个节点的位置是0+1就是1.
    """
    def height(self, root: TreeNode):
        if not root:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left)-self.height(root.right)) < 2 \
               and self.isBalanced(root.left) \
               and self.isBalanced(root.right)
