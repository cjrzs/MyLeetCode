"""
coding: utf8
@time: 2020/10/23 22:57
@author: cjr
@file: 回文链表.py
题目链接：https://leetcode-cn.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        先遍历全都放到数组里判断
        时间复杂度：O(n) 空间复杂度：O(n) 用了额外数组
        :param head:
        :return:
        """
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        i, j = 0, len(tmp) - 1
        while i <= j:
            if tmp[i] == tmp[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def isPalindrome2(self, head: ListNode) -> bool:
        """
        先用快慢指针找到中点，然后反转后面的链表，最后再与原链表进行比较
        :param head:
        :return:
        """
        nod1, nod2 = head, head
        # 先快慢指针找到链表的中点nod1
        while nod2.next and nod2.next.next:
            nod1 = nod1.next
            nod2 = nod2.next.next
        # 然后反转后面的链表
        cur, pre = nod1.next, None
        while cur:
            tmp = cur.next
            # 把后一个指针指向前一个
            cur.next = pre
            # 两个指针依次后移
            pre = cur
            cur = tmp
        res = True
        first, second = head, pre
        while second and res:
            if first.val == second.val:
                first = first.next
                second = second.next
            else:
                res = False
        return res




