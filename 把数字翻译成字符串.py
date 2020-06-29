'''
coding:utf8
@Time : 2020/6/9 22:35
@Author : cjr
@File : 把数字翻译成字符串.py
题目链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
'''


class Solution:
    """
    这道题当dp[i] + dp[i+1] 在10到25之间的时候就是斐波那契数列
    如果不在这之间最后的结果并不会发生变化。
    （ps：其实只要列出五个数字找一下规律就可以简单的解出来）
    """
    def translateNum(self, num: int) -> int:
        num_str = str(num)
        a = 1
        b = 1

        for i in range(1, len(num_str)):
            flag = num_str[i - 1: i + 1]
            print(f'flag: {flag}')
            # if '10' <= flag <= '25':
            if "10" <= flag <= "25":
                res = a + b
            else:
                res = a
            print(f'a:{a}')
            b = a
            print(f'res:{res}')
            a = res
        return a


if __name__ == '__main__':
    com = Solution()
    res1 = com.translateNum(12258)
    print(res1)




