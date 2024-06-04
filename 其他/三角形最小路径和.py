'''
coding:utf8
@Time : 2020/7/14 11:01 
@Author : CJR  
@File : 三角形最小路径和.py
题目链接：https://leetcode-cn.com/problems/triangle/
'''
from typing import List


class Solution:
    """
    状态转移方程： dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j])
    当我们在i行的最左侧时，只能从第i-1行的最左侧移动过来，所以此时方程为：
    dp[i][i]=dp[i−1][i−1]+triangle[i][i]
    """
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        print(dp)
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
        print(dp)
        return min(dp[n - 1])


if __name__ == '__main__':
    com = Solution()
    print(com.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
