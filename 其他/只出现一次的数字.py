'''
coding:utf8
@Time : 2020/5/11 22:00
@Author : cjr
@File : 只出现一次的数字.py
题目链接：https://leetcode-cn.com/problems/single-number/
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''


class Solution:
    """
    题解：
    这就触及我的知识盲区了
    ^ 异或运算符
    0和任何数异或的结果都是这个数
    任何相同的数异或结果都是0
    因此偶数次出现的数异或为0，奇数次出现的异或为本身，因此遍历异或结果为唯一出现奇数次的数
    """
    def singleNumber(self, nums: list) -> int:
        a = 0
        for num in nums:
            a ^= num
        return a


if __name__ == '__main__':
    com = Solution()
    print(com.singleNumber([4,1,2,1,2]))


