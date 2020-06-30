'''
coding:utf8
@Time : 2020/6/30 23:52
@Author : cjr
@File : 用两个栈实现队列.py
题目链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
'''


class CQueue:
    """
    题目解析：
    只需要一个栈存，然后另外一个栈存另一个栈的倒序就可以了
    """

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1

        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

