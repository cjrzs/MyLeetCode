'''
coding:utf8
@Time : 2020/3/11 23:11
@Author : cjr
@File : 二进制求和.py
'''


class Solution:
    """
    本题思路就是当把两个数逐个相加，除以二取余 放在结果中即可
    """
    def addBinary(self, a: str, b: str) -> str:
        # 二进制数长度
        i = len(a) - 1
        j = len(b) - 1
        # 进位
        carry = 0
        # 结果
        res = ""
        # 根据数字长短和进位来操作
        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            # 获取当前位的结果
            res = str(carry % 2) + res
            # 进位操作,向下取整
            carry //= 2
        return res


if __name__ == '__main__':
    com = Solution()
    print(com.addBinary("11111", "0000"))

