'''
coding:utf8
@Time : 2020/4/18 22:56
@Author : cjr
@File : 路径总和.py
本题链接：https://leetcode-cn.com/problems/path-sum/
'''

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        2020.07.07的每日一题，又做了一遍
        DFS.
        一直向下遍历找到叶子节点，判断是否与sum相等
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

