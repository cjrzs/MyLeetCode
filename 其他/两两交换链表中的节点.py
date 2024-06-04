"""
coding:utf8
@Time : : 2020/10/22 13:53
@Author : CJR
@File : 两两交换链表中的节点.py
"""
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        直接递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        new = head.next
        head.next = self.swapPairs(new.next)
        new.next = head
        return new

    def swapPairs2(self, head: ListNode) -> ListNode:
        """
        设置一个哨兵节点
        :param head:
        :return:
        """
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while tmp.next and tmp.next.next:
            nod1 = tmp.next
            nod2 = tmp.next.next
            tmp.next = nod2
            nod1.next = nod2.next
            nod2.next = nod1
            tmp = nod1
        return dummy.next

