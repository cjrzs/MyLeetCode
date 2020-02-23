'''
coding:utf8
@Time : 2020/2/24 0:02
@Author : cjr
@File : 移除元素.py
题目链接：https://leetcode-cn.com/problems/remove-element/
'''


class Solution:
    """
    本题明确说明要在原地修改数组长度，而不可以新建一个数组，而且可以忽略新数组长度后面的元素，
    那么我们其实只要覆盖原数组就可以了，把与目标不同的数字放在最前面，遍历一遍之后只需要返回
    覆盖部分的长度。
    空间复杂度:O(1)
    时间复杂度:O(n)
    题解解析：
    1、定义头指针
    2、遍历数组
    3、如果不是目标元素
    4、将不是目标元素的放在头指针
    5、头指针向后位移一位
    """
    def removeElement(self, nums: list, val: int) -> int:
        flag = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[flag] = nums[i]
                flag += 1
        return flag
