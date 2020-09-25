"""
coding: utf8
@time: 2020/9/25 23:42
@author: cjr
@file: 从中序与后序遍历序列构造二叉树.py
题目链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        先根据后序遍历和中序遍历的规则，找出两个数组的特点。依据其特点转化成二叉树
        1、后序遍历的最后一位必然是最终根节点，获取根节点
        2、中序遍历的左子树和右子树，可以遍历中序遍历列表，通过根节点的值获取。根节点左面是左子树，右面是右子树
        3、依据上面条件进行递归。可以获取到两个数组对应的状态
        4、postart -->  postart+leftsize  -->  |postend。
        ----------左子树----------------右子树--| 根节点

        instart  -->  |index|  -->  inend
        -----左子树----|根节点|---右子树---
        依据这个图填入正确索引即可
        参考文档：https://mp.weixin.qq.com/s/OlpaDhPDTJlQ5MJ8tsARlA
        :param inorder:
        :param postorder:
        :return:
        """
        def helper(inorder, instart, inend, postorder, postart, poend):
            if instart > inend:
                return None
            root_val = postorder[poend]
            index = 0
            for i in range(instart, inend + 1):
                if inorder[i] == root_val:
                    index = i
                    break
            left_size = index - instart
            root = TreeNode(root_val)
            root.left = helper(inorder, instart, index - 1, postorder, postart, postart + left_size - 1)
            root.right = helper(inorder, index + 1, inend, postorder, postart + left_size, poend - 1)
            return root
        return helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
