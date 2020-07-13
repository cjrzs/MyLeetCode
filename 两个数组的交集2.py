'''
coding:utf8
@Time : 2020/7/13 10:48 
@Author : CJR  
@File : 两个数组的交集2.py
题目链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/
'''
from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        使用collections计数，取交集
        时间复杂度：O(m+n)
        空间复杂度：O(min(m, n))
        :param nums1:
        :param nums2:
        :return:
        """
        ans = []
        dic1 = collections.Counter(nums1)
        print(f'dic1: {dic1}')
        dic2 = collections.Counter(nums2)
        print(f'dic2: {dic2}')
        num = dic1 & dic2
        for i in num.elements():
            ans.append(i)
        return ans

    # 进阶：如果给定的数组已经排好序呢？你将如何优化你的算法？
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        使用两个指针，判断两个集合里的元素是否相等
        元素小的那个集合指针后移
        时间复杂度：O(m+n)
        空间复杂度：O(min(m, n))
        :param nums1:
        :param nums2:
        :return:
        """
        ans = list()
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        m = len(nums2)
        index1 = index2 = 0
        while index1 < n and index2 < m:
            print(f'index1: {index1}, index2: {index2}')
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                ans.append(nums1[index1])
                index1 += 1
                index2 += 1
        return ans


if __name__ == '__main__':
    com = Solution()
    print(com.intersect2(nums1 = [1,2,2,1], nums2 = [2,2]))
