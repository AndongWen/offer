'''表示数值的字符串:
	请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
	例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
	但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。'''
class Solution:
	def isNumeric1(self, s):
	# 骚操作:将字符串转换成浮点数
		try:
			ss = float(s)
			return True
		except:
			return False
	# 也可以使用re的正则表达式来匹配
	def isNumeric(self, s):
		self.s = s
		self.l = len(s)
		if self.l == 0:
			return False
		return self.isNumericCore(0)

	def isNumericCore(self, i):
		numeric = self.scanInteger(i)[0]
		j = self.scanInteger(i)[1]
		if j < self.l and self.s[j] == '.':
			j += 1
			# 0.123 123.都对，即.前后只要有一边有数字即可
			numeric = self.scanUnsignInteger(j)[0] or numeric 
			j= self.scanUnsignInteger(j)[1]
		if j < self.l and self.s[j] in {'e','E'}:
			j += 1
			# eE前后必须都有数字
			numeric = self.scanInteger(j)[0] and numeric
			j = self.scanInteger(j)[1]
		return numeric and self.l == j

	def scanInteger(self, index):
		if index < self.l and self.s[index] in {'+', '-'}:
			index += 1
		return self.scanUnsignInteger(index)

	def scanUnsignInteger(self, index):
		mark = index
		while index < self.l and self.s[index] >= '0' and self.s[index] <= '9':
			index += 1
		return (bool(index>mark), index)
s = Solution()
print(s.isNumeric('12e'))
