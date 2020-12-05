"""
coding: utf8
@time: 2020/12/4 21:29
@author: cjr
@file: 分割数组为连续子序列.py
题目链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/
"""
from typing import List
from collections import defaultdict
import heapq


class Solution:

    def isPossible(self, nums: List[int]) -> bool:
        mp = defaultdict(list)
        for num in nums:
            queue = mp.get(num - 1)
            if queue:
                level = heapq.heappop(queue)
                heapq.heappush(mp[num], level + 1)
            else:
                heapq.heappush(mp[num], 1)
        return not any(queue and queue[0] < 3 for queue in mp.values())



