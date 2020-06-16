'''
coding:utf8
@Time : 2020/6/16 23:19
@Author : cjr
@File : 二叉树的序列化与反序列化.py
题目链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    前序遍历
    题解看注释
    """
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        # 前序遍历二叉树，空节点添加null占位，放在res中
        def serialize(root):
            if root is None:
                res.append('null')
            else:
                res.append(str(root.val))
                serialize(root.left)
                serialize(root.right)
        # 进行遍历，得到遍历好的res
        serialize(root)
        # 转成字符串
        res = ','.join(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        # 字符串空直接返回空数组
        if not data:
            return []
        # 因为用','链接的，这里用','分隔成数组
        data = data.split(',')

        # 反序列化，返回值是数组下标与与其值
        def deserialize(index):
            # 如果值是该下标对应的val是null说明，这个节点为空
            if data[index] == 'null':
                return index, None
            else:
                # 我们从跟节点开始遍历
                node = TreeNode(int(data[index]))
                # 左节点为根节点加一
                l, left = deserialize(index + 1)
                node.left = left
                # 右节点为左节点加一
                r, right = deserialize(l + 1)
                node.right = right
                # 返回他们的下标和对应值
                return r, node
        # 因为deserialize返回了两个值，一个是下标一个是node，我们要取node所以是
        return deserialize(0)[1]


if __name__ == '__main__':
    codec = Codec()
    codec.deserialize(codec.serialize(TreeNode()))
