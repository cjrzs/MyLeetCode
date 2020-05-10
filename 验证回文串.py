'''
coding:utf8
@Time : 2020/5/10 21:50
@Author : cjr
@File : 验证回文串.py
题目链接：https://leetcode-cn.com/problems/valid-palindrome/
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
'''
import re


class Solution:
    """
    好简单 好简单  简单到没啥好说的了
    第一个是伪代码  用的双指针
    第二个python切片
    """
    def isPalindrome(self, s: str) -> bool:
        new_ls = []
        for i in s:
            is_str = re.findall('\w|\d', i, re.S)
            if is_str:
                new_ls.append(i)
        new_s = ''.join(new_ls).lower()
        print(new_s)
        if not new_s:
            return True
        elif len(new_s) == 1:
            return True
        start = 0
        end = len(new_s) - 1
        flag = False
        while end >= start:
            if new_s[end] == new_s[start]:
                flag = True
                start += 1
                end -= 1
            else:
                flag = False
                return flag
        return flag


def isPalindrome2(self, s: str) -> bool:
    new_ls = []
    for i in s:
        is_str = re.findall('\w|\d', i, re.S)
        if is_str:
            new_ls.append(i)
    new_s = ''.join(new_ls).lower()
    print(new_s)
    if new_s == new_s[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    com = Solution()
    print(com.isPalindrome('race a car'))

