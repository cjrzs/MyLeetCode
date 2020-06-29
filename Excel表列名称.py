'''
coding:utf8
@Time : 2020/5/16 21:30
@Author : cjr
@File : Excel表列名称.py
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    # def convertToTitle(self, n: int) -> str:
    #     com = Solution()
    #     if n == 1:
    #         res = 'A'
    #     elif n < 26:
    #         while n > 1:
    #             tmp = n % 26
    #             res = ord('A') + int(tmp) - 1
    #             res = chr(res)
    #             n = n / 26
    #     elif n == 26:
    #         res = 'Z'
    #     elif n > 26:
    #         n /= 26
    #         tmp = n % 26 + 1
    #         res2 = com.convertToTitle(n)
    #         res3 = com.convertToTitle(tmp)
    #         res = res2 + res3

        # return res

    def convertToTitle2(self, n: int) -> str:
        t = n
        s = ''
        while t > 0:  # 每次循环 是 每次取模得到数字 的过程
            t -= 1  # 把 从1开始满27进位 变回 从0开始满26进位
            a, b = t // 26, t % 26  # 这里b的取值范围是0-25
            print(a, b)
            s = s + chr(b + 65)  # A的ASCII码是65，b+65表示 0-25 和 A-Z 有了一一对应
            t = a
        return s[::-1]


if __name__ == '__main__':
    com = Solution()
    print(com.convertToTitle2(701))











