"""
coding:utf8
@Time : : 2020/10/12 16:43
@Author : CJR
@File : 二叉搜索树的最小绝对差.py
题目链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        中序遍历，遍历好之后放在数组内，两两组合取出最小值，即可。
        :param root:
        :return:
        """
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
            return nums
        nums = []
        dfs(root)
        res = float('inf')
        for i in range(1, len(nums)):
            res = min(res, nums[i]-nums[i-1])
        return res
