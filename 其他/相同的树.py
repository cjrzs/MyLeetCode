'''
coding:utf8
@Time : 2020/3/22 0:40
@Author : cjr
@File : 相同的树.py
题目链接：https://leetcode-cn.com/problems/same-tree/
'''
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    题解思路:利用递归，暴力思路
    如果q，p全空，那么自然完全相等返回True
    如果有一个空，那么返回False
    递归判断下一个节点
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        DFS
        时间复杂度： O(min(m,n)) m和n 是p和q的深度
        空间复杂度： O(min(m,n)) m和n 是p和q的深度
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(q.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        BFS
        c
        :param p:
        :param q:
        :return:
        """
        if not p and not q:
            return True
        if not p or not q:
            return False

        queue1 = collections.deque([q])
        queue2 = collections.deque([p])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False
            if left1:
                queue1.append(left1)
            if right1:
                queue1.append(right1)
            if left2:
                queue2.append(left2)
            if right2:
                queue2.append(right2)

        return not queue1 and not queue2



if __name__ == '__main__':
    x = Solution()
    print(x.isSameTree2([1,2,3], [1,2,3]))


