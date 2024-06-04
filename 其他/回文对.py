"""
coding:utf8
@Time : 2020/8/6 10:59 
@Author : CJR  
@File : 回文对.py
题目链接：https://leetcode-cn.com/problems/palindrome-pairs/submissions/
"""
from typing import List


class Solution:

    @staticmethod
    def palindrome_pairs(words: List[str]) -> List[List[int]]:
        """
        时间复杂度：O(n^2*m) m是单词的平均长度
        空间复杂度：O(n*m) n是words长度，m是单词的平均长度
        :param words:
        :return:
        """

        # 初始化一个字典存储每个字符串的下标， 初始化一个空列表存结果
        lookup = {w: i for i, w in enumerate(words)}
        res = []
        # 对单词列表进行循环
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                # 将每个单词分成前缀、后缀两部分
                pre, suf = w[j:], w[:j]
                # 如果前缀是回文串，那么只要后缀的倒序在words中存在就可以组成回文串
                # 后缀不能等于w，是因为要去掉当前缀空时候，整个w本身就是一个回文串的这种情况
                # （PS：这个如何分析需要弄几个例子根据代码跑一遍，就能理解）
                if pre[::-1] == pre and suf[::-1] in lookup and suf != w:
                    # 当满足条件把后缀的倒序放在前面，当前串在后面，即可组成新的回文串
                    res.append([lookup[suf[::-1]], i])
                if suf[::-1] == suf and pre[::-1] in lookup and pre != w and j != len(w):
                    res.append([i, lookup[pre[::-1]]])
        return res



if __name__ == '__main__':
    x = Solution()
    x.palindrome_pairs(["abcd","dcba","lls","s","sssll"])
