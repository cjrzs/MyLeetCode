'''
coding:utf8
@Time : 2020/5/13 22:42
@Author : cjr
@File : 环形链表.py
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    快慢指针法
    设置两个指针同时从头结点出发，
    慢指针走一步，快指针走两步
    如果成环，两指针必然相遇。
    当快指针走到尾（快指针为空）还没有相遇说明没有成环。
    """
    def hasCycle(self, head: ListNode) -> bool:
        slow = quick = head
        while quick and quick.next:    # 使用while来确定快指针是否为空和头结点是否为空
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False

