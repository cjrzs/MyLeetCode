'''
coding:utf8
@Time : 2020/7/4 16:25
@Author : cjr
@File : 最长有效括号.py
题目链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        栈解法：
        初始化：栈为-1，避免当第一个字符就是），出栈没有元素报错；同时避免所有括号全部匹配时候计算长度少1.
        入栈条件：当前括号为左括号
        出栈条件：当前括号为右括号
        计算子串长度条件：当前栈不为空，栈内有元素
        计算方法：当前元素 - 栈底元素 并且更新最大值
        :param s:
        :return:
        """
        n = len(s)
        stack = [-1]
        ans = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
                continue
            else:
                stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])
        return ans

    def longestValidParentheses2(self, s: str) -> int:
        """
        动态龟化参考的官方题解
        :param s:
        :return:
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                # 在这里2代表当前i对应的一对括号，dp[i-1]代表的是i-1对应的括号
                # 最后的dp[i - dp[i - 1] - 2] 代表的是他俩前面的括号子串
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        return max(dp)


if __name__ == '__main__':
    com = Solution()
    print(com.longestValidParentheses("()(()"))




