'''调整数组顺序，使得奇数在偶数前面：
	输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
	使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
	并保证奇数和奇数，偶数和偶数之间的相对位置不变。'''
class Solution():
	def reOrderArray(self, array):
		# 使用两个指针，分别从数组的前后遍历指针，当前指针指向的数
		# 为偶数，后指针指向的数为奇数，此时交换两者，类似快排
		if not array:
			return 
		p1, p2 = 0, len(array)-1
		while p1 < p2:
			while p1 < len(array) and array[p1]%2 == 1:
				p1 += 1
			while p2 >= 0 and array[p2]%2 == 0:
				p2 -= 1
			if p1 >= p2:
				break
			if p1 < len(array) and p2 >= 0:
				array[p1], array[p2] = array[p2], array[p1]
				p1 += 1
				p2 -= 1
	
s = Solution()
a = [1,2,3,4,5,6,7]
s.reOrderArray(a)
print(a)	
