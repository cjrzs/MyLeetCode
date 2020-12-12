"""
coding:utf8
@Time : 2020/7/25 23:37
@Author : cjr
@File : 字符串的好分割数目.py
给你一个字符串 s ，一个分割被称为 「好分割」 当它满足：将 s 分割成 2 个字符串 p 和 q ，它们连接起来等于 s 且 p 和 q 中不同字符的数目相同。

请你返回 s 中好分割的数目。



示例 1：

输入：s = "aacaba"
输出：2
解释：总共有 5 种分割字符串 "aacaba" 的方法，其中 2 种是好分割。
("a", "acaba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
("aa", "caba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
("aac", "aba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
("aaca", "ba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
("aacab", "a") 左边字符串和右边字符串分别包含 3 个和 1 个不同的字符。
示例 2：

输入：s = "abcd"
输出：1
解释：好分割为将字符串分割成 ("ab", "cd") 。
示例 3：

输入：s = "aaaaa"
输出：4
解释：所有分割都是好分割。
示例 4：

输入：s = "acbadbaada"
输出：2


提示：

s 只包含小写英文字母。
1 <= s.length <= 10^5
"""


class Solution:
    def numSplits(self, s: str) -> int:
        """
        暴力解法 时间复杂度O(n^2) TQL
        :param s:
        :return:
        """
        ans = 0

        def count_s(s1):
            res = 0
            count_res = []
            for i1 in range(len(s1)):
                if not count_res or s1[i1] not in count_res:
                    count_res.append(s1[i1])
                    res += 1
            return res

        for i in range(len(s)):
            before = count_s(s[0: i])
            end = count_s(s[i: len(s) + 1])
            if before == end:
                ans += 1
        return ans


a = 9453252335432530000000000000000000000000
b = 9453252335432530000000000000000000000000
if __name__ == '__main__':
    # com = Solution()
    # print(com.numSplits("acbadbaada"))
    print(id(a))
    print(id(b))


