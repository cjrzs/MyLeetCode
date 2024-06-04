'''
coding:utf8
@Time : 2020/7/5 21:02
@Author : cjr
@File : 通配符匹配.py
题目链接：https://leetcode-cn.com/problems/wildcard-matching/
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        zong = len(p) + 1  # 纵轴长度
        heng = len(s) + 1  # 横轴长度

        table = [[False] * heng for i in range(zong)]
        table[0][0] = True
        print(f'初始化table：{table}')

        if p.startswith("*"):
            table[1] = [True] * heng

        for m in range(1, zong):
            path = False  # 是否可以在该行使用*的特技
            for n in range(1, heng):
                if p[m - 1] == "*":  # m是表格的索引，但不是p的索引
                    if table[m - 1][0] == True:
                        table[m] = [True] * heng
                    if table[m - 1][n]:  # 只要顶上有了True，就可以开通*接下来的所有道路
                        path = True
                    if path:
                        table[m][n] = True
                elif p[m - 1] == "?" or p[m - 1] == s[n - 1]:  # 先判断字母是否符合
                    table[m][n] = table[m - 1][n - 1]  # 再看左上方格子是不是T

        return table[zong - 1][heng - 1]


if __name__ == '__main__':
    com = Solution()
    print(com.isMatch(s="aa", p="a"))
