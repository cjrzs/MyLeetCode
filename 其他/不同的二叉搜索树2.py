'''
coding:utf8
@Time : 2020/7/21 21:49
@Author : cjr
@File : 不同的二叉搜索树2.py
题目链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
'''
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    二叉搜索树的特性：
    右边的数大于当前根节点
    左边的数小于当前根节点
    没有重复的值
    """
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTrees(start, end):
            if start > end:
                return [None]
            # 根据题意，遍历1到n个根节点。
            all_trees = []
            for i in range(start, end + 1):
                # 左右节点也需要遍历
                left = generateTrees(start, i - 1)
                right = generateTrees(i + 1, end)
                # 选择左右节点的二叉搜索树
                for l in left:
                    for r in right:
                        # 把所有节点组成的二叉树全放在结果中
                        tree = TreeNode(i)
                        tree.left = l
                        tree.right = r
                        all_trees.append(tree)
            return all_trees
        return generateTrees(1, n) if n else []


