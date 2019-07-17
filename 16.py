'''给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。'''
'''可以直接使用pow()函数；
	使用递归，时间复杂度为O(logN)
	当n为偶数, a^n = a^(n/2) * a^(n/2)
	当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
	利用右移一位运算代替除以2
	利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
	优化代码速度'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 1:
            return base
        if exponent == 0:
            return 1
        isNegative = False
        if exponent < 0:
            isNegative = True
            exponent = -exponent
        pow = self.Power(base, exponent>>1)
        pow *= pow
        if exponent & 0x01:
            pow *= base
        return 1/pow if isNegative else pow
