'''输入一个链表，输出该链表中倒数第k个结点。'''
class Solution():
	def FindKthToTail(self, head, k):
		# 双指针法，先让一个指针跑k步，再让两个指针一起跑，当先跑的指针到达尾部时，慢指针所指的节点就是倒数第k个节点
		if not head or k <= 0:
			return None
		fast = head # 此时fast指针已经走了一步
		for i in range(k-1):
			if fast.next != None:
				fast = fast.next 
			else: # 此时fast指针已经到达尾部，但是k步没有走完，说明k值大于链表的长度，即非法输入
				return None
		slow = head
		while fast.next:
			fast = fast.next
			slow = slow.next
		return slow	
