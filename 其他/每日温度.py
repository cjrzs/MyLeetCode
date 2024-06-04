'''
coding:utf8
@Time : 2020/6/11 23:00
@Author : cjr
@File : 每日温度.py
题目链接：https://leetcode-cn.com/problems/daily-temperatures/
'''
import typing


class Solution:
    def dailyTemperatures(self, T: typing.List[int]) -> typing.List[int]:
        # 可以维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减。
        # 如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标。

        """
        其实只需要走一遍就能理解流程。主要利用的就是列表的pop与append，也就是栈这个数据结构。
        :param T:
        :return:
        """
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:  # 栈不为空 && 栈顶温度小于当前温度
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans


if __name__ == '__main__':
    com = Solution()
    print(com.dailyTemperatures([73,74,75,71,69,72,76,73]))
