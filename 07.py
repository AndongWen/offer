'''输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 通过前序遍历的第一个节点就是根节点来在中序遍历中将树分为左子树和右子树，递归
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        return self.helper(pre, tin, 0, len(pre)-1, 0)
    
    def helper(self, pre, tin, preL, preR, inL):
		#　inL为中序遍历中左子树的第一个节点数值
        if preL > preR:
            return None
        root = TreeNode(pre[preL])
        inindex = tin.index(root.val)
        leftlen = inindex - inL
        root.left = self.helper(pre, tin, preL+1, preL+leftlen, inL)
        root.right = self.helper(pre, tin, preL+leftlen+1, preR, inL+leftlen+1)
        return root
