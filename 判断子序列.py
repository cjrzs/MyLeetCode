'''
coding:utf8
@Time : 2020/7/19 17:04
@Author : cjr
@File : 判断子序列.py
题目链接：https://leetcode-cn.com/problems/is-subsequence/
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        唔， 2020-07-27每日一题 又做了一遍

        双指针：
        两个指针从0开始遍历两个字符串
        如果两个指针的值相等两个指针均后移
        如果不相等s的指针原地等待匹配，t的指针后移
        最后判断s的指针与s的字符串长度是否相等。

        时间复杂度：O(n + m),因为需要把n和m全部遍历一遍
        空间复杂度：O(1)，没有利用到额外空间
        :param s:
        :param t:
        :return:
        """
        i = j = 0
        n, m = len(t), len(s)
        while i < n and j < m:
            if t[i] == s[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == m


    def isSubsequence2(self, s: str, t: str) -> bool:
        """
        动态规划，预处理字符串t， 找到每个字符第一次出现在t中的位置
        :param s:
        :param t:
        :return:
        """
        n, m = len(s), len(t)
        # 初始化DP，因为当前字符出现位置依赖于下一个字符位置
        # 所以我们需要从后往前遍历， 因此初始化最后的数组
        dp = [[0] * 26 for _ in range(m)]
        dp.append([m] * 26)
        # dp数组表示从i开始往后字符j出现的位置
        # 当i位置的字符和j相等时候dp[i][j] == i
        # 否则状态转移方程：dp[i][j] == dp[i + 1][j]
        for i in range(m - 1, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(t[i]) == j + ord('a') else dp[i + 1][j]

        # add表示的是当前位置。初始化是0，下一次是【（t中 s的第一个字符） + 1】
        add = 0
        for i in range(n):
            # 对于边界状态 f[m−1][..]，我们置f[m][..] 为 m，让f[m−1][..] 正常进行转移。
            # 这样如果f[i][j]=m，则表示从位置 i 开始往后不存在字符 j。
            if dp[add][ord(s[i]) - ord('a')] == m:
                return False

            add = dp[add][ord(s[i]) - ord('a')] + 1

        return True


if __name__ == '__main__':
    com = Solution()
    print(com.isSubsequence2("abc", "ahbgdc"))

