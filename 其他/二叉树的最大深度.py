'''
coding:utf8
@Time : 2020/4/3 0:41
@Author : cjr
@File : 二叉树的最大深度.py
题目连接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    抄袭一下官方题解吧
    实在看不懂递归，使用下面的迭代的方法
    判断输入根节点是否空，不空则将该节点的深度和本身放入stack
    初始深度0，犹豫每次都要判断左右节点，所以限制条件stack为空才可以结束进行下一轮判断
    """
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root:
                depth = max(current_depth, depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return depth

    def maxDepth2(self, root: TreeNode) -> int:
        """
        递归方法。
        :param root:
        :return:
        """
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) + 1
# if __name__ == '__main__':
#     com = Solution()
#     res = com.maxDepth(TreeNode("[3,9,20,null,null,15,7]"))
#     print(res)

