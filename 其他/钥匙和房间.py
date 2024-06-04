"""
coding:utf8
@Time : 2020/8/31 11:42 
@Author : CJR  
@File : 钥匙和房间.py
题目链接：https://leetcode-cn.com/problems/keys-and-rooms/
"""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        dfs.
        时间复杂度：O(n+m) n是房间，m是房间内钥匙的数量
        空间复杂度：O(n) 房间的数量，dfs所需要的栈的开销
        :param rooms:
        :return:
        """
        def dfs(x):
            # 使用set数组标记已经搜索过的房间
            vis.add(x)
            nonlocal num
            # num表示走过房间的个数
            num += 1
            for i in rooms[x]:
                if i not in vis:
                    dfs(i)
        vis = set()
        num = 0
        n = len(rooms)
        # 从0开始走。 如果最后走过的房间和所有房间数相等，则为true，反之为false
        dfs(0)
        return n == num

