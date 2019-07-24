'''343.给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 
	返回你可以获得的最大乘积。'''
'''思路：
		1.动态规划　特点：1.求解问题为最优解问题，且问题可以分为若干子问题，
							同时子问题的之间还有相互重叠的问题
						  2.整体问题的最优解依赖于子问题的最优解
						  3.大问题分成若干小问题，小问题之间还有相互重复的更小的
						　　的子问题
					      4.为了避免在解决大问题时重复解决小问题，所以将小问题的解
							存储起来。从上到下分析问题，从下到上解决问题
		对于n，进行拆分的时候有n-1种选择，需要进行计算找到对应的最大值
		
		2.贪婪算法:每次拆分的时候都找最优的选择，由数学证明可以得到当n>=5时，每次
				　　拆出3，可以使解答最优'''
class Solution:
    def integerBreak(self, n: int) -> int:
		#　贪婪算法
		res = 1
		if n < 2:
			return 0
		elif n == 2:
			return 1
		elif n == 3:
			return 2
		elif n == 4:
			return 4
		else:
			while n > 4:
				res *= 3
				n -= 3
		return res*n

class Solution:
    def integerBreak(self, n: int) -> int:
		# 动态规划
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        res = [0] * (n+1)
        res[0] = 0
        res[1] = 1
        res[2] = 2
        res[3] = 3
        for i in range(4, n+1):
            max_res = 0
            for j in range(1, i//2+1):
                max_res = max(res[j] * res[i-j], max_res)
            res[i] = max_res
            
        return res[n]
