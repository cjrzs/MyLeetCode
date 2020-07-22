"""
coding:utf8
@Time : 2020/7/22 12:42 
@Author : CJR  
@File : 旋转数组的最小数字.py
题目链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
"""
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        """
        二分查找
        :param numbers:
        :return:
        """
        start = 0
        end = len(numbers) - 1
        while start < end:

            mid = start + (end - start) // 2
            # 如果中值小于最后一个值，那么说明中值后面的值都比最小值大，所以可以把尾指针给中值指针
            if numbers[mid] < numbers[end]:
                end = mid
            # 如果大于的话说中值前面的值都比中值小，所以移动start指针到中值指针后面
            elif numbers[mid] > numbers[end]:
                start = mid + 1
            # 因为会有重复元素的情况 所以当中值和最后的值相等 说明出现重复元素  把最后的值指针向前一位即可。
            else:
                end -= 1
        # 因为初始指针在移动之后回找到最小的值，所以只需要返回初始指针。
        return numbers[start]

