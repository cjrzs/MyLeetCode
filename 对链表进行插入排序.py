"""
coding: utf8
@time: 2020/11/20 15:06
@author: cjr
@file: 对链表进行插入排序.py
题目链接：https://leetcode-cn.com/problems/insertion-sort-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        时间复杂度需要遍历两次链表，所以是O(n)
        :param head:
        :return:
        """
        cur = head
        dummy = ListNode(0)  # 初始化一个虚拟头节点
        pre = dummy
        while cur:
            # 循环中值不小于当前值时候就需要插入当前值了。
            while cur.next and pre.next.val < cur.val:
                pre = pre.next
            # 先记录当前节点的下一个节点，因为本次循环结束后，要把当前节点移动到下一个节点
            this = cur.next
            # 下面两步就是插入啦，需要在纸上画一下，就能理解了。
            cur.next = pre.next
            pre.next = cur
            # 插入之后，两个指针整体复原，pre继续回归头节点，因为下一个值的插入也需要从dummy开始检测
            # 而当前节点cur，就直接往后移动就可以了
            pre = dummy
            cur = this
        return dummy.next
















