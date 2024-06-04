'''
coding:utf8
@Time : 2020/5/24 18:48
@Author : cjr
@File : 最长回文子串.py
题目链接：https://leetcode-cn.com/problems/longest-palindromic-substring/
'''


class Solution:
    """
    曹尼玛 不会了
    """
    def longestPalindrome(self, s: str) -> str:
        res = ''
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for l in range(n):
            for i in range(n):
                j = i + 1
                if j > len(s):
                     break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and l + 1 > len(res):
                    res = s[i:j+1]
        return res


if __name__ == '__main__':
    con = Solution()
    print(con.longestPalindrome('babab'))



