'''
coding:utf8
@Time : 2020/2/17 22:52
@Author : cjr
@File : 有效的括号.py
题目链接：https://leetcode-cn.com/problems/valid-parentheses/
'''


class Solution:
    """
    本题有以下几个关键点：

    1、括号的匹配规则符合栈先入后出的结构，即最后进入的括号与他的前一个互相匹配
    如果匹配成功则弹出前一个进入的括号。

    2、思路：

    a、我们以不同括号创建字典，再创建一个列表stack。字典的key为左括号，value为右括号。

    b、遍历所以输入的字符串s，如果在s中的字符i在字典的key中，也就是是左括号我们放入stack

    c、如果不是左括号，则为右括号，也就是字典的value，我们弹出（pop）列表stack中一个
    元素，该元素的value如果与字典中的value一样匹配成功，程序继续执行，如果不一样匹配失败，
    说明不是有效括号，返回False

    d、最后程序的画龙点睛之笔是在最后判断stack的长度，如果是初始长度说明全部匹配成功（匹配
    成功则弹出，所以stack应为初始长度）。如果不是初始长度说明有未匹配的括号，那么输入的字符
    串s不是有效括号。
    （PS：程序中的？用作边界检测。如果输入的第一个括号就是右括号，那么会直接pop，这时候如果
    如果stack中没有元素会报错，因此我们用一个？占位）
    """
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}", "?": "?"}
        stack = ["?"]
        for i in s:
            if i in d.keys():
                stack.append(i)
            elif d[stack.pop()] != i:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    str1 = "(()("
    com = Solution()
    print(com.isValid(str1))







