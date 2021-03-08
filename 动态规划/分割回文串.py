"""
coding: utf8
@time: 2021/3/8 21:52
@author: cjr
@file: 分割回文串.py
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
通过次数90,319提交次数124,0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    这道题的细节，在于使用动态规划先计算出每个子串是不是回文串，这个操作很简单核心原理就是
    dp[i, j]中只要s[i] == s[j] 那么只要他们的里面一层也就是dp[i + 1, j - 1]也是回文串
    说明dp[i, j]也是回文串。
    处理好之后我们就知道那些子串是回文串了。然后利用回溯遍历所有可组成的子串就行了，把是子串的放进去。
    """
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]

        res, tmp = [], []

        def dfs(i):
            if i == n:
                res.append(tmp[:])
                return
            for j in range(i, n):
                if f[i][j]:
                    tmp.append(s[i: j + 1])
                    dfs(j + 1)
                    tmp.pop()
        dfs(0)
        return res




