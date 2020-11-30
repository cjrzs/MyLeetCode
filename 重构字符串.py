"""
coding: utf8
@time: 2020/11/30 22:38
@author: cjr
@file: 重构字符串.py
题目链接：https://leetcode-cn.com/problems/reorganize-string/
"""
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        if n < 2:
            return S
        counts = Counter(S)
        res = []
        max_count = max(counts.items(), key=lambda x: x[1])[1]
        if max_count > (n + 1) // 2:
            return ''
        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        while len(queue) > 1:
            # 弹出两个元素，这样两个元素必定不同，且出现个数是最多和次多的。
            _, item1 = heapq.heappop(queue)
            _, item2 = heapq.heappop(queue)
            # 把两个元素拼接到res
            res.extend([item1, item2])
            # 因为两个元素已经拼接完，所以计数分别减一
            counts[item1] -= 1
            counts[item2] -= 1
            # 如果这两个元素个数还大于0，还要把它们加入堆，再拼接这两个元素，直到所有元素都拼接完
            # （此处体现了贪心的思路，每次都拼接最大的和次大的）
            if counts[item1] > 0:
                heapq.heappush(queue, (-counts[item1], item1))
            if counts[item2] > 0:
                heapq.heappush(queue, (-counts[item2], item2))
        # 最后要判断一下还剩一个元素的情况。
        if queue:
            res.append(queue[0][1])
        return ''.join(res)






