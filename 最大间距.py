"""
coding: utf8
@time: 2020/11/26 15:26
@author: cjr
@file: 最大间距.py
题目链接：https://leetcode-cn.com/problems/maximum-gap/
"""
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        直接使用桶排序
        :param nums:
        :return:
        """
        # 先算出来整个数组中的最大，最小值
        max_ = max(nums)
        min_ = min(nums)
        n = len(nums)
        if n < 2:
            return 0
        each_bucket_size = max((max_ - min_) // (n - 1), 1)
        buckets = [[] for _ in range((max_ - min_) // each_bucket_size + 1)]

        for i in range(n):
            loc = (nums[i] - min_) // each_bucket_size
            buckets[loc].append(nums[i])
        # 用当前区间的最小值，减去上一个区间的最大值就是相邻元素的最大差值
        res = 0
        # 记录上一个的最大值
        prev_max = float('inf')
        for i in range(len(buckets)):
            # 求当前区间最小值和上一个区间最大值的差值，和目前的最大差值作比较，更新最大差值
            if buckets[i] and prev_max != float('inf'):
                res = max(res, min(buckets[i]) - prev_max)
            if buckets[i]:
                # 当前元素的最大值给上一个
                prev_max = max(buckets[i])
        return res




