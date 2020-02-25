'''
coding:utf8
@Time : 2020/2/26 0:05
@Author : cjr
@File : 实现strStr().py
题目链接：https://leetcode-cn.com/problems/implement-strstr/
'''


class Solution:
    """
    本题其实很简单抛出去那些高难度的字符串匹配算法（比如kmp，动态规划之类的），我们可以
    先排除特殊情况，然后根据长度逐个比较即可
    题解思路：
    1、第一二行定义两个字符串长度
    2、第三四五六行抛出去特殊情况
    3、第七行定义起始标志0
    4、第八行确定判断次数
    5、其后几行，判断从0开始到与needle串长度相等的这部分子串是否与needle本身相等
    如果相等则直接返回标志位的值，就是我们要的结果，如果不相等则将标志位后移一位。
    所有结果判断完仍然没有相等的返回-1
    """
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        lh = len(haystack)
        if ln == 0:
            return 0
        elif ln == lh and haystack != needle:
            return -1
        i = 0
        while i <= lh-ln:
            if haystack[i:i+ln] == needle:
                return i
            else:
                i += 1
        return -1


if __name__ == '__main__':
    com = Solution()
    res = com.strStr("mississippi", "pi")
    print(res)
