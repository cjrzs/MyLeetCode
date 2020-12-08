"""
coding: utf8
@time: 2020/12/5 14:49
@author: cjr
@file: 任务调度器.py
题目链接：https://leetcode-cn.com/problems/task-scheduler/
"""
from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        max_sum = counts[0][1]
        res = (max_sum - 1) * (n + 1)
        for task in counts:
            if task[1] == max_sum:
                res += 1
        return res if res >= len(tasks) else len(tasks)
