"""
coding: utf8
@time: 2020/11/16 20:36
@author: cjr
@file: 根据身高重建队列.py
题目链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        # 先排序，根据身高降序排序，然后根据第二个元素升序排序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        for p in people:
            # 如果结果中的数量小于等于当前第二个元素，说明当前元素应该排在最后，这样它前面的人数才小于等于它
            if len(res) <= p[1]:
                res.append(p)
            # 如果大于元素直接把元素插入到p[1]的位置，这样就可以保证他前面有p[1]个人了
            else:
                res.insert(p[1], p)
        return res


