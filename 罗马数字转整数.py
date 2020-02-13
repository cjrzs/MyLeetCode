'''
@Time: 2020/2/13
@Author: cjr
@File: 罗马数字转整数
题目链接：https://leetcode-cn.com/problems/roman-to-integer/
'''


class Solution:
    """
    抄袭大佬的解法，真的是太优秀了
    首先有几个关键点：
    1、dict.get(key, defult=None),这个方法中的key可以是一个列表
    2、本题的第22行就是获取了列表的value，如果dict1中没有这个列表那么默认取当前value
    3、遍历时候会依次遍历，举个例子如果输入的是I，那么先遍历I取到值1，向后遍历到如果是V
    那么就会和前面的I组成一个列表IV正好对应dict1中的值3，这样与前面I的值1相加就是4正好
    得到IV的值！
    """
    def romanToInt(self, s: str) -> int:
        dict1 = {"I": 1, "IV": 3, "V": 5, "IX": 8, "X": 10,
                 "XL": 30, "L": 50, "XC": 80, "C": 100,
                 "CD": 300, "D": 500, "CM": 800, "M": 1000}
        list1 = []
        for x, y in enumerate(s):
            int1 = dict1.get(s[x - 1: x + 1], dict1[y])
            list1.append(int1)
        result = sum(list1)
        return result


