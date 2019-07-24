'''输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，
	则打印出 1、2、3 一直到最大的 3 位数即 999。'''
'''思路:在python中显然可以选择直接用循环将所有符合条件的数字打印出来，因为在python中
		int不是四字节的，没有固定的大小；一般性的，我们需要考虑n过大的情况，所以选择用
		字符串或者数组来表示这个数字'''
class Solution(object):
	def PrintToMaxOfNDigits(self, n):
		# 用字符串模拟加法，进行输出
		if n <= 0:
			return 
		num = ['0'] * n # 数组内的元素也可以是数字
		while not self.Increment(num):
			self.PrintNum(num)

	def Increment(self, num): # 判断最高位是否有进位，有则返回为True 平均时间复杂度O(n)
		isOverFlow = False
		nCarry = 0 # 进位
		nLength = len(num)
		
		for i in range(nLength-1, -1, -1):
			nSum = int(num[i]) + nCarry 
			if i == nLength-1: # 保证每次调用函数Increment时，数字只增加1
				nSum += 1 # 模拟数字的加１
			if nSum >= 10:
				if i == 0:
					isOverFlow = True
				else:
					nSum -= 10
					nCarry = 1
					num[i] = str(nSum)
			else:
				num[i] = str(nSum)
				break
		return isOverFlow

	def PrintNum(self, num):
		nLen = len(num)
		isStartWith0 = True
		for i in range(nLen):
			if isStartWith0 and num[i] != '0':
				isStartWith0 = False
			if not isStartWith0:
				print('%s' % num[i], end='')
		print('')

	def PrintToMaxOfNDigits2(self, n):
		# 实际就是n位数字上的0-9的全排列，可以使用递归来完成、
		if n <= 0:
			return 
		num = ['0']*n
		for i in range(10):
			num[0] = str(i) # 最高位
			self.PrintToMaxOfNDigitsRecursively(num, n, 1)

	def PrintToMaxOfNDigitsRecursively(self, num, length, index):
		if index == length:
			self.PrintNum(num)
			return
		for i in range(10):
			num[index] = str(i)
			self.PrintToMaxOfNDigitsRecursively(num, length, index+1)	
		
def main():
	s = Solution()
	s.PrintToMaxOfNDigits2(14)

if __name__ == '__main__':
	main()
