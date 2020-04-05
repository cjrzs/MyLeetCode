'''
coding:utf8
@Time : 2020/4/6 0:14
@Author : cjr
@File : 二叉树的层序遍历2.py
题目链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题解思路：
    使用递归的方法，用一个字典存储层数和该层的值（值为列表），
    如果该层在字典中那么把节点值append入字典
    如果不在则将其存到该层
    然后先左后右递归
    最后倒序输出存的节点值即可
    """
    def levelOrderBottom(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []
        res = {}

        def dfs(r, n):
            if n in res:
                res[n].append(r.val)
            else:
                res[n] = [r.val]
            if r.left:
                dfs(r.left, n+1)
            if r.right:
                dfs(r.right, n+1)

        dfs(root, 1)
        result = [res[k] for k in sorted(res.keys(), key=lambda x:x, reverse=True)]
        return result


