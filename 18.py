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

class Solution:
    def deleteDuplication(self, pHead):
	'''普通方法:使用两个指针，一个curNode用于遍历整个链表，一个preNode为curNode的
	前一个节点(初始值为None)，当cur.next存在且curNode.val==cur.next.val，
	说明有节点需要被删除，然后从curNode开始遍历寻找到一个与当前节点值不同的节点，
	但此节点仍需要检查(后续节点的值是否与他相等);反之，只需要将preNode与curNode后移
	即可'''
		if not pHead:
			return pHead
		
		preNode = None # 当前遍历节点的前一个节点
		curNode = pHead # 当前遍历节点
		while curNode:
			nextNode = cur.next
			if nextNode and nextNode.val == curNode.val: # 从curNode开始需要删除
				tobeDel = curNode
				tobeDelVal = curNode.val
				while tobeDel and tobeDel.val == tobeDelVal:
					tobeDel = tobeDel.next
				if not preNode: # 说明重复的节点是从头结点开始的
					pHead = tobeDel # 修改头部节点
					curNode = tobeDel	
					continue # 此时新的头部节点仍需要进行检查
				else:
					preNode.next = tobeDel
					curNode = preNode
			else:
				preNode = curNode
				curNode = curNode.next
	
		return pHead
