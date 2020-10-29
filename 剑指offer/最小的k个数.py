"""
coding: utf8
@time: 2020/10/29 23:04
@author: cjr
@file: 最小的k个数.py
题目链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
"""
import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 处理k为0的特殊情况
        if k == 0:
            return []
        # 因为python的headp维护的是最小堆，所以要把前k个数的负数放到堆里
        hp = [-x for x in arr[0: k]]
        heapq.heapify(hp)
        # 遍历剩下的去和堆顶比较，把较大的移出去，较小的数放到堆里
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappushpop(hp, -arr[i])
        # 然后再变回来正数
        ans = [-x for x in hp]
        return ans
