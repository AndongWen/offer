'''在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here 递归每次寻找一个不重复的节点，并将其返回
        if not pHead or not pHead.next:
            return pHead
        next = pHead.next
        if next.val == pHead.val:
            while next and pHead.val == next.val: # 寻找到第一个与pHead.val不同的值或者到链表的末尾
                next = next.next
            return self.deleteDuplication(next)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead
