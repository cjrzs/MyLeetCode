"""
coding: utf8
@time: 2021/3/10 23:04
@author: cjr
@file: 基本计算器.py
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

 

示例 1：

输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 2-1 + 2 "
输出：3
示例 3：

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23
 

提示：

1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    """
    思路:
    1. 如果字符是数字，则开始计算当前数字
    2. 如果字符是符号(+ or -) 那么开始计算当前字符前面的结果
    3. 如果是左括号，说明需要优先计算口号内的内容，先把当前结果和左括号前面的符号入栈
       然后把结果和当前符号全部重置，开始括号内的计算。
    4. 如果遇到了右括号，说明括号内的表达式已经可以计算好了，我们先把右括号前面的结果
       计算完成，这样就完成了括号内的计算，然后重置当前值（num），把栈中的符号弹出来，
       在把前面的结果弹出来和括号内计算出来的结果加一起。
    5. 最后别忘记最后计算一次结果。
    """
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+' or c == '-':
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += num * sign
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += num * sign
        return res








