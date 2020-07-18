'''
coding:utf8
@Time : 2020/7/18 18:39
@Author : cjr
@File : 交错字符串.py
题目链接：https://leetcode-cn.com/problems/interleaving-string/
'''


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        # 如果两个字符串的长度加起来不等于第三个，那么肯定是False
        if len1 + len2 != len3:
            return False
        # 初始化DP，s1是横坐标，s2是纵坐标，初始化[0][0]为True
        dp = [[False]*(len2+1) for _ in range(len1+1)]
        dp[0][0] = True

        for i in range(1, len1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])
        for i in range(1, len2+1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        return dp[-1][-1]



