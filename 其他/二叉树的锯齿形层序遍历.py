"""
coding: utf8
@time: 2020/12/22 23:47
@author: cjr
@file: 二叉树的锯齿形层序遍历.py
题目链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        直接使用双端队列deque，模拟遍历过程。
        :param root:
        :return:
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        x = 0
        while queue:
            size = len(queue)
            i = 0
            level = []
            while i < size:
                # 当在偶数层时候。从首位弹出，并且入队遵循先左后右
                if x & 1 == 0:
                    tmp = queue.popleft()
                    if tmp.left:
                        queue.append(tmp.left)
                    if tmp.right:
                        queue.append(tmp.right)
                # 当在奇数层时候。从尾部弹出，并且入队遵循先右再左。
                else:
                    tmp = queue.pop()
                    if tmp.right:
                        queue.appendleft(tmp.right)
                    if tmp.left:
                        queue.appendleft(tmp.left)
                level.append(tmp.val)
                i += 1
            res.append(level)
            x += 1
        return res

    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        """
        大佬的思路。
        使用一个标记位，标记当前在那一层，True为偶数层，False为奇数层
        :param root:
        :return:
        """
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        lr = True
        while deque:
            size = len(queue)
            level = [0] * size
            i = 0
            while size > i:
                print(lr)
                # 下面两句代码的意思是：
                # 1、每次都从首部弹出，
                # 2、如果是偶数层就从前往后放，如果是奇数层就从后往前放
                root = queue.popleft()
                level[i if lr else size - i - 1] = root.val
                # 正常的将左右入队
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                i += 1
            res.append(level)
            # 遍历过一层之后要转变标志位。
            lr = (not lr)
        return res




