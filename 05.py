'''将一个字符串中的空格替换成 "%20"。'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        '''由于python中str为不可哈希的，所以无法向其他语言一样在源字符串中直接修改
		　 java中使用双指针,先统计源字符串中空格数目，一个空格就需要在末尾添加任意两
		   字符，p1为源字符串的末尾p2为当前字符串的末尾，从后向前遍历，s[p1]为空格
		   s[p2]依次添加'02%'，反之直接将s[p1]复制过来。下面的code仿照此算法写的'''
        p1 = len(s) - 1
        res = ''
        while p1 >= 0:
            if s[p1] == ' ':
                res = '%20' + res
            else:
                res = s[p1] + res
            p1 -= 1
        return res

def main():
	so = Solution()
	res1 = so.replaceSpace('we we ')
	print(res1)
	res1 = so.replaceSpace('  ')
	print(res1)
	res1 = so.replaceSpace('we  we ')
	print(res1)
	res1 = so.replaceSpace('we we   ')
	print(res1)
	res1 = so.replaceSpace('we we ')
	print(res1)
	res1 = so.replaceSpace('we we ')
	print(res1)
	res1 = so.replaceSpace('we we ')
	print(res1)
	res1 = so.replaceSpace('we we ')
	print(res1)

if __name__ == "__main__":
	main()
