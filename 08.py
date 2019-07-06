'''给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。'''
'''如果此节点有右孩子，则在中序遍历中下一个节点就是此右孩子的最左边的节点；
	如果没有右边孩子，就需要上溯，找到第一个左链接指向的树包含该节点的祖先节点。'''
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node
        else:
            while pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
        return None #　防止给的是根节点，同时右子树为空
