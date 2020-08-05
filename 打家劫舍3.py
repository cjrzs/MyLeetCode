"""
coding:utf8
@Time : 2020/8/5 11:29 
@Author : CJR  
@File : 打家劫舍3.py
题目链接：https://leetcode-cn.com/problems/house-robber-iii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob1(self, root: TreeNode) -> int:
        """
        暴力法，会超时
        根据题意，计算两种情况。
        将二叉树分为根节点和子节点和孙子节点
        因为题中说明不能项链根节点不能偷了则子节点不能偷。

        第一种情况是：偷根节点和所有的孙子节点
        第二种情况是：偷两个子节点
        计算出这两种情况进行比较就可以了。
        （PS：这种情况时间复杂度特别高，会超时）
        :param root:
        :return:
        """
        if not root:
            return 0

        money = root.val

        if root.left != None:
            money += (self.rob(root.left.left) + self.rob(root.left.right))

        if root.right != None:
            money += (self.rob(root.right.left) + self.rob(root.right.right))

        return max(money, self.rob(root.left) + self.rob(root.right))

    def rob2(self, root: TreeNode) -> int:
        """
        这种做法，完全不看孙子节点。根据偷不偷根节点分成两种情况。
        偷根节点：两个子节点就不能偷。money = 左子节点不偷 + 右子节点不偷 + 根节点的val
        不偷根节点：那就取两个（子节点就可以偷也可以不偷）
                  money = 左子节点偷 + 右子节点偷
        时间复杂度：O(n) 对二叉树做了一次遍历
        空间复杂度：O(1)
        :param root:
        :return:
        """
        def _rob(root):
            if not root:
                return 0, 0
            # ls是偷左子树的收益， ln是不偷左子树的收益，rs, rn同理是右子树
            ls, ln = _rob(root.left)
            rs, rn = _rob(root.right)

            return root.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(_rob(root))




