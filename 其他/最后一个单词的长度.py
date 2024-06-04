'''
coding:utf8
@Time : 2020/3/2 23:34
@Author : cjr
@File : 最后一个单词的长度.py
题目链接：https://leetcode-cn.com/problems/length-of-last-word/
'''


class Solution:
    """
    及其简单，随便讲一下理解算了。
    先处理s的前后空格，倒序遍历s，不是空结果就+1，是空就直接返回结果
    """
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        result = 0
        for i in s[-1::-1]:
            if i != " ":
                result += 1
            else:
                return result
        return result








