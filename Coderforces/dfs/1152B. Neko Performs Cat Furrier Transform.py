import sys
from collections import defaultdict, Counter

sys.setrecursionlimit(8 ** 10)
input = sys.stdin.readline

"""
题目本来不难，但是题意很难理解：

给出一个数 x ，可以其做一下两个操作：
1. 将 x = x ^ (2 ** k - 1);
2. 将 x += 1;
通过以上两个操作，使得 x 变成 (2 ** k - 1)。

这里主要的一个关键点是，明白 2**k-1 是什么意思。
注意 2**k 的二进制表示是 100..00(k个0) ，那么 减去1 就变成了 111...11(k个1)
而 x 异或上 k个1  就是把x的二进制表示的后k位取反。
而 x += 1 实际上就是让 x的二进制表示的最后一个0 变成1。

所以我们可以通过操作1 使得第一个0变成1，这样交替操作，一定可以使得 x 的二进制表示 变为全1。
"""
x = int(input())
cnt = 0
one = True
res = []
while x & (x + 1):
    if one:
        b = bin(x)[2: ]
        t = 0
        for c in b:
            t += 1
            if c == '0':
                break
        # print(b, len(b), t)
        num = (2 ** (len(b) - t + 1) - 1)
        res.append(str(len(b) - t + 1))
        x = x ^ num
    else:
        x = x + 1
    cnt += 1
    one = not one
print(cnt)
print(' '.join(res))

