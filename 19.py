'''正则表达式匹配:请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次
（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，
字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配'''
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        self.s = len(s)
        self.p = len(pattern)
        if self.s == 0 or self.p == 0:
            return False
        return self.matchCore(s, pattern, 0, 0)
    
    def matchCore(self, s, pattern, index_s, index_p):
        if index_p == self.p and index_s < self.s:
            return False
        if index_s == self.s and index_p == self.p:
            return True
        if index_p+1 < self.p and pattern[index_p+1] == '*':
            if s[index_s] == pattern[index_p] or (pattern[index_p] == '.' and index_s < self.s): # 表示这个位置的字符匹配
                return self.matchCore(s, pattern, index_s, index_p+2) \
                	or self.matchCore(s, pattern, index_s+1, index_p+2) \
                	or self.matchCore(s, pattern, index_s+1, index_p) 
            else:
                self.matchCore(s, pattern, index_s, index_p+2)
        if s[index_s] == pattern[index_p] or (pattern[index_p] == '.' and index_s < self.s):
            return self.matchCore(s, pattern, index_s+1, index_p+1)
        return False

    def isMatch(self, s, p): # ok
		# 暴力匹配
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0],  '.'}
        if len(p) >= 2 and p[1] == '*':
             return self.isMatch(s, p[2:]) or \
                 (first_match and self.isMatch(s[1:], p)) # 分别匹配0,1次
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch2(self, s, p):
		# 使用额外空间对结果进行存储,避免重复计算
        res = {}
        def dp(i, j): 
            if (i, j) in res:
                return res[(i, j)]
            if j == len(p):
                return i == len(s)
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p)-2 and p[j+1] == '*':
                ans = dp(i, j+2) or \
                    dp(i+1, j)
            else:
               ans = dp(i+1, j+1)
            res[(i, j)] = ans
            return ans

        return dp(0,0)

def main():
	s = Solution()
	a = s.isMatch2('baadc', 'c*.a*.c')
	print(a)

if __name__ == "__main__":
	main()
	
