'''
coding:utf8
@Time : 2020/2/19 23:29
@Author : cjr
@File : 合并两个有序链表.py
题目链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
'''


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    涉及到链表实在是不会了，感觉太难理解了，解释一下别人的大神解法
    该解法有以下几个关键点（行数以实际有效代码为准）：

    1、解法中运用了and和or，这两个都有阻断效果，and前面的表达式为False则后面的表达式不执行，
    or前面的表达式为True则后面的不执行。

    在这个解法里第一行如果l1为空那么下面第五行则返回l2，反之l2为空返回l1。
    如果l1、l2全部有值则进入第二行

    2、第二行则是该解法的精妙之处，判断了l1的值，如果l1的值大于l2则把l1与l2交换位置，实际上
    这个动作就是把较小的值放在l1里。

    3、第四行l1的下一个值递归了本函数，这里有一个坑，答主的题解中没有说明，导致了很难理解，就是
    其实本函数返回的永远是链表l1（除非l1为空），那么也就是说第一次执行之后如果l1的值比l2大，那
    么交换位置，l1就变成了较小的值,递归一次执行函数完成l1的排序，l2虽然有变化但是与结果无关。
    这样我们就可以正确获取较小的链表l1.
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

