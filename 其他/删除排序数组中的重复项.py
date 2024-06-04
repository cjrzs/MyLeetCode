'''
coding:utf8
@Time : 2020/2/20 23:42
@Author : cjr
@File : 删除排序数组中的重复项.py
'''


class Solution:
    """
    这道题还是蛮简单的，因为题目要求原地删除重复的元素，我们只需要用python里面的pop方法就可以了
    我们可以直接用逆向循环，正向循环无法判断结束点。由于是有序数组我们只需要逐个比较，pop掉相同
    的即可完成。

    看了下大佬们说要用双指针，其实双指针也是最快的，有时间会更新一个双指针题解
    """
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        for i in range(len(nums))[::-1]:
            if i-1 != -1:
                if nums[i] == nums[i-1]:
                    nums.pop(i)
        print(nums)
        return len(nums)


if __name__ == '__main__':
    com = Solution()
    length = com.removeDuplicates([1, 1, 2])
    print(length)










