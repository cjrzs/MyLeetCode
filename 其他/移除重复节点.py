'''
coding:utf8
@Time : 2020/6/26 18:22
@Author : cjr
@File : 移除重复节点.py
题目链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
'''
import typing


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    题解：设置一个缓存区，遍历节点，如果节点的值在缓存区里有就把该节点的指针指向他的下一个节点
          如果缓存区中没有就把这个节点值放在缓存区。
    """
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head

        pos = head
        occurred = {head.val}

        while pos.next:
            cur = pos.next
            if cur.val not in occurred:
                occurred.add(cur.val)
                pos = pos.next
            else:
                pos.next = pos.next.next
        return head





