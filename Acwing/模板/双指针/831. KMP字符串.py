"""
coding: utf8
@time: 2021/1/26 16:23
@author: cjr
@file: 831. KMP字符串.py
给定一个模式串S，以及一个模板串P，所有字符串中只包含大小写英文字母以及阿拉伯数字。

模板串P在模式串S中多次作为子串出现。

求出模板串P在模式串S中所有出现的位置的起始下标。

输入格式
第一行输入整数N，表示字符串P的长度。

第二行输入字符串P。

第三行输入整数M，表示字符串S的长度。

第四行输入字符串S。

输出格式
共一行，输出所有出现位置的起始下标（下标从0开始计数），整数之间用空格隔开。

数据范围
1≤N≤105
1≤M≤106
输入样例：
3
aba
5
ababa
输出样例：
0 2
"""

n = int(input())
p = ' ' + str(input())
m = int(input())
s = ' ' + str(input())

# 先搞出next数组, next数组中的元素含义为：
# 以next[i]为例，表示用来匹配的字符串P中，截至到i为止 前缀与后缀相等的情况下，前缀（后缀）的最大值
ne = [0] * (n + 1)
j = 0
for i in range(2, n + 1):
    # 如果j不是空且 前缀字符和后缀字符不等则j = ne[j]  (此处仍不明觉厉)
    while j and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j

j = 1
for i in range(1, m + 1):
    while j and s[i] != p[j + 1]:
        j = ne[j]
    if s[i] == p[j + 1]:
        j += 1
    # 成功找到一个字符串
    if j == n:
        print(i - n, end=' ')
        j = ne[j]











