'''
coding:utf8
@Time : 2020/7/12 22:01
@Author : cjr
@File : 地下城游戏.py
题目链接：https://leetcode-cn.com/problems/dungeon-game/
'''
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        // 走路分为两步：
        // 0. 当前，设为x，血量大于0
        // 1. 走到下一个格子。血量增加了dungenon[i][j]
        // 2. 从下一个格子走到终点。需要的血量为int val = Math.min(dp[i+1][j], dp[i][j+1]);
        // 所以有 x + dungenon[i][j] = val
        // 所以有 x = val - dungenon[i][j]
        :param dungeon:
        :return:
        """
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[10**9] * (m + 1) for _ in range(n + 1)]
        dp[n - 1][m] = dp[n][m - 1] = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # 最小值只有两种情况下面和右面
                minn = min(dp[i + 1][j], dp[i][j + 1])
                # 当前值如注释所示
                dp[i][j] = max(minn - dungeon[i][j], 1)
        return dp[0][0]

