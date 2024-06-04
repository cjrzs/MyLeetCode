'''
coding:utf8
@Time : 2020/6/25 19:42
@Author : cjr
@File : 单词拆分.py
题目链接：https://leetcode-cn.com/problems/word-break/
'''
import typing


class Solution:
    # 题解参考链接：
    def wordBreak(self, s: str, wordDict: typing.List[str]) -> bool:
        # 使用动态规划， 初始化dp数组， 第一位为True，方便进入循环
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        # 遍历S
        for i in range(len(s)):
            # 每次遍历都从True位置开始，因为以前的子串都不在wordDict中，无须遍历
            if dp[i] is True:
                # i与字符串s中的每一个字符j组成新的子串，如果该子串在wordDict中，我们把dp中的j位置变成True
                for j in range(i + 1, len(s) + 1):
                    if s[i: j] in wordDict:
                        dp[j] = True
        # 结果这里如果dp最后一个元素是True那么我们认为，所有的wordDict中的元素都能在s的子串中找到
        return dp[-1]

