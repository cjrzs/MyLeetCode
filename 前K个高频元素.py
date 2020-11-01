"""
coding: utf8
@time: 2020/11/1 9:52
@author: cjr
@file: 前K个高频元素.py
题目链接：https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 初始化一个放入顶堆的数组
        heap_max = []
        # 初始化一个存放值与个数的hash
        dic = {}
        # 初始化一个结果数组
        res = []
        # 循环遍历将给出的nums中每个值都对应上各自的个数（[1,1,1,2,2,3], 2）
        # 循环结束后dic中为{1: 3, 2: 2, 3: 1} 前面是元素后面是该元素的个数
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        # 循环dic中的元素放入顶堆，值和字典的元素用数组的形式放进去
        # 此时循环结束后heap_max的值是[(-3, 1), (-2, 2), (-1, 3)]
        for i in dic:
            heapq.heappush(heap_max, (-dic[i], i))
        # 最后循环k次取出k个堆顶元素（堆顶最大）放在结果里就行了
        for _ in range(k):
            tmp = heapq.heappop(heap_max)
            res.append(tmp[1])
        return res






