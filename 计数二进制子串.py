"""
coding:utf8
@Time : 2020/8/10 11:29 
@Author : CJR  
@File : 计数二进制子串.py
题目链接：https://leetcode-cn.com/problems/count-binary-substrings/
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        将每个只包含纯0或纯1的部分存起来
        然后两两相比较，将较小的相加就是结果
        （PS：这题像个脑筋急转弯，转不过来就很难理解了）
        目前时空复杂度都是 O（n）,空间复杂度不用counts存储结果可以优化成O(1)
        :param s:
        :return:
        """
        counts = []
        n, m = 0, len(s)
        while n < m:
            count = 0
            tmp = s[n]
            while n < m and s[n] == tmp:
                n += 1
                count += 1
            counts.append(count)
        print(f'counts: {counts}')
        res = 0
        for i in range(1, len(counts)):
            # print(i)
            res += min(counts[i], counts[i - 1])
        return res


if __name__ == '__main__':
    x = Solution()
    print(x.countBinarySubstrings("00110"))
