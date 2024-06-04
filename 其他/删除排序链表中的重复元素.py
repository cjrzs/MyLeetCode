'''
coding:utf8
@Time : 2020/3/18 23:48
@Author : cjr
@File : 删除排序链表中的重复元素.py
题目链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    思路：主要就是注意空指针的情况，其他没什么特殊的。
    当前值和下一个值相等时候，当前指针指向下下个值即可
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr != None and curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head




