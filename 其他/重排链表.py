"""
coding: utf8
@time: 2020/10/20 23:14
@author: cjr
@file: 重排链表.py
题目链接：https://leetcode-cn.com/problems/reorder-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找到中心点
        point1, point2 = head, head
        while point2:
            point1 = point1.next
            point2 = point2.next.next
        # 反转后半部分链表
        cur, pre = None, point1.next
        point1.next = None
        while pre:
            t = pre.next
            pre.next = cur
            cur, pre = pre, t
        # 相交组合
        p, q = head, cur
        while p:
            t = p.next
            p.next = q
            p = q
            q = t



