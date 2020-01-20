'''
coding:utf8
@Time : 2020/1/20 10:21 
@Author : CJR  
@File : 解压缩编码列表.py    
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
'''


class Solution:

    def decompressRLElist(self, nums: list) -> list:
        """
        思路就是找出偶数下标的元素做为个数
        然后下标+1的元素做为值传到新列表就行了
        :param nums:
        :return:
        """
        new_nums = []
        for i in range(len(nums)):
            if i % 2 == 0:
                for x in range(nums[i]):
                    new_nums.append(nums[i+1] )
        return new_nums


if __name__ == '__main__':
    c = Solution()
    l = c.decompressRLElist([1,2,3,4])
    print(l)

