'''
coding:utf8
@Time : 2020/7/6 11:50 
@Author : CJR  
@File : 不同路径 II.py
题目链接：https://leetcode-cn.com/problems/unique-paths-ii/
'''
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) # m是纵坐标
        if m == 0:
            return 0
        n = len(obstacleGrid[0]) # n是横坐标

        dp = [[0] * n for _ in range(m)]
        # 因为初始点的左和上 都没办法走  所以我们把初始点设置成1
        dp[0][0] = 1
        # 预先处理第一行和第一列
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
        # 核心状态转移方程：dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # 因为[i][j]的值只取决于他的左上两个位置
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    print(dp)

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    com = Solution()
    print(com.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
