'''
coding:utf8
@Time : 2020/4/7 23:10
@Author : cjr
@File : 将有序数组转换为二叉搜索树.py
题目链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题解：
    高度平衡二叉搜索树：
    1、若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值
    2、若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值
    3、任意节点的左、右子树也分别为二叉搜索树
    4、没有键值相等的节点
    因为数组是有序的，所以我们选择中间的数为跟节点，左边的小放在左子节点，右边大放在右子节点
    然后递归到输入的节点是空 即可
    """
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root



