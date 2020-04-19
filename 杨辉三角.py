'''
coding:utf8
@Time : 2020/4/19 23:11
@Author : cjr
@File : 杨辉三角.py
题目链接：https://leetcode-cn.com/problems/pascals-triangle/
'''

"""
本题解析：
利用题目中的一个规律，就是当前一行错开一位相加之后就可以得到下一行，
例如第一行是1，那么我们把1错位相加 就是[0,1] + [1,0]就可以得到下一行[1,1]
然后[1,1]错误相加就是[0,1,1] + [1,1,0] = [1,2,1]就是下一行
只要使用这个规律就很简单了
"""


class Solution:

    def generate(self, numRows: int):

        res = [[1]]
        if numRows == 0:
            return []
        while len(res) < numRows:
            new_nums = [a+b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(new_nums)
        return res


if __name__ == '__main__':
    res = Solution()
    res2 = res.generate(5)
    print(res2)






