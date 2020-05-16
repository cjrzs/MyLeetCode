'''
coding:utf8
@Time : 2020/5/16 20:27
@Author : cjr
@File : 链表相交.py
编写一个程序，找到两个单链表相交的起始节点。

示例 1：

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    写个题解记录一下。
    这个处理方法很简单，就是用两个指针分别遍历两个两个链表
    因为两个链表有可能长度不一致，这就像两个不同的数a，b一样
    虽然数字不同，但是a+b一定与b+a相同。但是这里还有两个相交部分c，
    就变成了a+c+b == b+c+a。
    实际上走完a+b的距离时候，两个指针所处的位置就是题目中要求的相交点位置
    只要看这个就懂了：
    https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/lian-biao-xiang-jiao-shuang-zhi-zhen-onshi-jian-fu/
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


