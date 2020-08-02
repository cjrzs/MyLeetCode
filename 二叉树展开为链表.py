"""
coding:utf8
@Time : 2020/8/2 23:39
@Author : cjr
@File : 二叉树展开为链表.py
题目链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        寻找前驱节点方法
        """
        # 初始根节点为当前节点
        curr = root
        # 当当前节点不为空时进入循环
        while curr:
            # 如果当前节点有左子节点
            if curr.left:
                # 设置当前节点为前驱节点
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                # 将当前节点的右子节点赋给前驱节点的右子节点
                predecessor.right = curr.right
                # 当前节点的左子节点设置为空
                curr.left = None
                # 将当前节点的左子节点给当前节点的右子节点
                curr.right = nxt
            # 继续处理下一个节点
            curr = curr.right
