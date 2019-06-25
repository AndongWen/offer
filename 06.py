'''从尾巴遍历链表'''
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.res = []
        
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode:
            self.printListFromTailToHead(listNode.next)
            self.res.append(listNode.val)
        return self.res

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.res = []
        
    def printListFromTailToHead(self, listNode):
        # write code here
        # 头插法
        head = None
        while listNode:
            node = listNode.next
            listNode.next = head
            head = listNode
            listNode = node
        while head:
            self.res.append(head.val)
            head = head.next
        return self.res

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here 使用栈
        res = []
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        while stack:
            res.append(stack.pop(0))
        return res
