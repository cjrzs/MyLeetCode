'''
coding:utf8
@Time : 2020/7/9 23:30
@Author : cjr
@File : 恢复空格.py
题目链接：https://leetcode-cn.com/problems/re-space-lcci/
'''
from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        """
        题解：动态规划解法。
        初始化dp为sentence长度+1的数组
        设置i为当前字符所对应的最少未识别字符数，因为如果当前字符未识别，那么就要相当于前一个字符（i-1）加一
        所以我们可以直到状态转移方程：dp[i] = dp[i-1] + 1
        然后我们遍历出来所有[0:i]中的字符j与i组成子串如果在dictionary说明此时子串[j:i]不是未识别的字符
        我们j给dp与i给dp做比较min(dp[i],dp[j])，把当前最小的字符数给dp[i]
        结果我们取最后一个即可。
        :param dictionary:
        :param sentence:
        :return:
        """
        d = {}.fromkeys(dictionary)
        n = len(sentence)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in d:
                    f[i] = min(f[i], f[j])
        return f[-1]

