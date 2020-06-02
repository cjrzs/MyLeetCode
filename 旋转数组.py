'''
coding:utf8
@Time : 2020/6/2 22:45
@Author : cjr
@File : 旋转数组.py
题目链接：https://leetcode-cn.com/problems/rotate-array/
'''
import typing


class Solution:
    def rotate(self, nums: typing.List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        直接使用切片的方法，重新组合数组，不过因为使用了切片，利用了额外空间
        空间复杂度不符合O(1)要求
        """
        n = len(nums)
        # 因为k是非负整数，取余操作防止k大于数组长度出现报错
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums

    def rotate2(self, nums: typing.List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        使用遍历后插入的方式，循环k次，把最后一个数插入到第一位
        在原数组中操作，空间复杂度符合要求
        """
        n = len(nums)
        # 因为k是非负整数，取余操作防止k大于数组长度出现报错
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums

    def rotate3(self, nums: typing.List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        三次翻转，将数组分成两部分
        例如[1,2,3,4,5,6,7] 3，我们分成第一部分[1,2,3,4] 即[0, n-k-1]
        第二部分是[5,6,7] 即[n-k,n-1]。
        （ps：减一是因为数组从0开始，那么数位数时候会多数一位需-1）
        我们将两部分都一次翻转，得到[4,3,2,1,7,6,5]
        再翻转整体，得到最终结果[5,6,7,1,2,3,4]
        （ps：空间复杂度为O(1),必然是牺牲了时间复杂度的）
        """
        n = len(nums)
        # 因为k是非负整数，取余操作防止k大于数组长度出现报错
        k %= n

        def swap(x, r):
            while x < r:
                nums[x], nums[r] = nums[r], nums[x]
                x += 1
                r -= 1
        swap(0, n-k-1)
        swap(n-k, n-1)
        swap(0, n-1)
        return nums


if __name__ == '__main__':
    com = Solution()
    print(com.rotate([1,2], 3))
