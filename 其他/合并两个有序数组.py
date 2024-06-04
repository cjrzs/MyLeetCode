'''
coding:utf8
@Time : 2020/3/19 23:49
@Author : cjr
@File : 合并两个有序数组.py
本题链接：https://leetcode-cn.com/problems/merge-sorted-array/
'''


class Solution:
    """
    官方题解，使用了内置函数。
    """
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        反向比较
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return:
        """
        # 从末尾获取两个指针,并为合并后的新的num1数组设置尾指针
        p1 = m-1
        p2 = n-1
        p = m+n-1
        # 当两个指针都大于等于0时候进行比较,把比较大的放在结果数组的最后
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        """
        两个指针必须要置0才能说明遍历了两个数组的所有内容，前面的while循环有可能是从p1条件退出，
        此时p2还没遍历完，所以此时对应的情况是p1中最小的数比p2当前的数大，
        所以最后将p2中剩余的数一次性拷贝到nums1的头部
        """
        nums1[:p2 + 1] = nums2[:p2 + 1]


