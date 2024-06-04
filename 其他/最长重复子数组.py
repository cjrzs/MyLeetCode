'''
coding:utf8
@Time : 2020/7/1 22:00
@Author : cjr
@File : 最长重复子数组.py
题目链接：https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
'''
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        dp解法:状态转移方程 dp[i][j] = dp[i+1][j+1] + 1
        因为dp[i][j]是由dp[i+1][j+1]+1得来的
        所以我们从后往前遍历
        :param A:
        :param B:
        :return:
        """
        n, m = len(A), len(B)
        dp = [[0]*(m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(dp[i][j], ans)
        return ans

    def findLength2(self, A: List[int], B: List[int]) -> int:
        """
        暴力法 三重循环 严重超时
        :param A:
        :param B:
        :return:
        """
        n, m = len(A), len(B)
        ans = 0
        for i in range(n):
            for j in range(m):
                k = 0
                while i+k < n and j+k < m and A[i + k] == B[j + k] :
                    k += 1
                ans = max(ans, k)
        return ans


if __name__ == '__main__':
    com = Solution()
    print(com.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
    print(com.findLength2([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))

