"""
coding: utf8
@time: 2020/10/20 22:55
@author: cjr
@file: 反转链表.py
题目链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归方法
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        cur = self.reverseList(head.next)
        # head的下一个节点的下一个节点指向了head
        head.next.next = head
        # 然后把原来head的下一个节点置空
        head.next = None
        return cur

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        双指针
        使用中间节点存储以前的值，
        把当前节点的next指向前面，然后把两个指针依次后移
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        cur, pre = None, head
        while pre:
            t = pre.next
            pre.next = cur
            cur, pre = pre, t
        return cur

