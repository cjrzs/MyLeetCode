'''
coding:utf8
@Time : 2020/6/23 0:21
@Author : cjr
@File : 无重复字符的最长子串.py
题目链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lev = []
        # mi = 0
        stack = []
        for i in range(len(s)):
            print(f'index:{i}, n:{s[i]}')
            while i < len(s) and s[i] not in stack:
                stack.append(s[i])
                print(f'stack:{stack}')
                # mi += 1
                print(f'mx:{len(stack)}')
                i += 1
            lev.append(len(stack))
            stack = []
            # mi = 0
            # print(lev)
        return max(lev)


if __name__ == '__main__':
    com = Solution()
    print(com.lengthOfLongestSubstring("pwwkew"))

