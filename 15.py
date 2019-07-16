'''计算一个二进制数中１的位数'''
'''python中整数不是４个字节的，需要手动设置为32,因此只能使用n&1计算末尾的一位数是否为
	1，然后n左移'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        self.cnt = 0
        for i in range(32):
            self.cnt += n&1
            n >>= 1
        return self.cnt

'''提供另一种思路：n&(n-1)是去掉低位的1，所以n&=(n-1),当n不为0时，循环继续，每次循环
	计数加１'''
