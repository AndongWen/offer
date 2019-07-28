'''调整数组顺序，使得奇数在偶数前面：
	输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
	使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
	并保证奇数和奇数，偶数和偶数之间的相对位置不变。'''
class Solution():
	def reOrderArray(self, array):
		# 使用两个指针，分别从数组的前后遍历指针，当前指针指向的数
		# 为偶数，后指针指向的数为奇数，此时交换两者，类似快排
		# 但是这种方法会打乱奇数，偶数彼此之间的相互顺序
		if not array:
			return 
		pBegin, pEnd = 0, len(array)-1
		while pBegin < pEnd:
			while pBegin < len(array) and array[pBegin]&0x1== 1:
				pBegin += 1
			while pEnd >= 0 and array[pEnd]&0x1 == 0:
				pEnd -= 1
			if pBegin >= pEnd:
				break
			if pBegin < len(array) and pEnd >= 0:
				array[pBegin], array[pEnd] = array[pEnd], array[pBegin]
				pBegin += 1
				pEnd -= 1
	
	def reOrderArray2(self, array):
		# 不改变彼此之间的相互顺序
		left = [x for x in array if x&0x1]
		right = [x for x in array if not x&0x1]
		return left+right

	def reOrderArray3(self, array, length, func):
		if length < 2:
			return array
		pBegin, pEnd = 0, length-1
		while pBegin < pEnd:
			while pBegin < length and func(array[pBegin]):
				pBegin += 1
			while pEnd >= 0 and not func(array[pEnd]):
				pEnd -= 1
			if pBegin >= pEnd:
				break
			if pBegin < length and pEnd >= 0:
				array[pBegin], array[pEnd] = array[pEnd], array[pBegin]
				pBegin += 1
				pEnd -= 1
		return array

	def reOrderOddEven(self, array):
		length = len(array)
		return self.reOrderArray3(array, length, self.IsOdd)

	def IsOdd(self, n):
		return n&0x1

s = Solution()
a = [1,2,3,4,5,6,7]
s.reOrderOddEven(a)
print(a)	
