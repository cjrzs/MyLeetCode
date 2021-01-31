"""
coding: utf8
@time: 2021/1/31 15:21
@author: cjr
@file: Trie.py
维护一个字符串集合，支持两种操作：

“I x”向集合中插入一个字符串x；
“Q x”询问一个字符串在集合中出现了多少次。
共有N个操作，输入的字符串总长度不超过 105，字符串仅包含小写英文字母。

输入格式
第一行包含整数N，表示操作数。

接下来N行，每行包含一个操作指令，指令为”I x”或”Q x”中的一种。

输出格式
对于每个询问指令”Q x”，都要输出一个整数作为结果，表示x在集合中出现的次数。

每个结果占一行。

数据范围
1≤N≤2∗104
输入样例：
5
I abc
Q abc
Q ab
I ab
Q ab
输出样例：
1
0
1
"""


class TrieTree:

    def __init__(self, n):
        self.p = [[0] * 26 for _ in range(n + 1)]
        self.idx = 0
        self.cnt = [0] * (n + 1)

    def insert(self, s):
        x = 0
        for i in s:
            u = ord(i) - ord('a')
            if self.p[x][u] == 0:
                self.idx += 1
                self.p[x][u] = self.idx
            x = self.p[x][u]
        self.cnt[x] += 1

    def query(self, s):
        x = 0
        for i in s:
            u = ord(i) - ord('a')
            if self.p[x][u] == 0:
                return 0
            x = self.p[x][u]
        return self.cnt[x]


if __name__ == '__main__':
    n = int(input())
    tt = TrieTree(n)
    for i in range(n):
        x, y = input().split()
        if x == 'I':
            tt.insert(y)
        else:
            print(tt.query(y))






