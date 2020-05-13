'''
coding:utf8
@Time : 2020/5/13 23:07
@Author : cjr
@File : 两数之和2.py
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    """
    使用双指针的方法
    首尾两个数相加与目标值做比较
    如果比目标值大那就尾指针-1
    如果比目标值小就头指针+1
    """
    def twoSum(self, numbers: list, target: int) -> list:
        start = 0
        end = len(numbers) - 1
        while end > start:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start + 1, end + 1]


if __name__ == '__main__':
    com = Solution()
    res = com.twoSum([2,7,11,15], 9)
    print(res)




