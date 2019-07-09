'''矩阵中的路径:请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，
向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子
之后，路径不能再次进入该格子。'''
'''回溯法：使用递归'''
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows < 1 or cols < 1 or path == '':
            return False
        str_ma = self.build(matrix, rows, cols)
        print(str_ma)
        mark = [[False for _ in range(cols)] for _ in range(rows)]
        pathlen = 0
        for i in range(rows):
            for j in range(cols):
                if self.backtracking(str_ma, mark, rows, cols, i, j, path, pathlen):
                    return True
        return False
    
    def build(self, matrix, rows, cols):
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(len(matrix)):
            res[i//cols][i%cols] = matrix[i]
        return res
    
    def backtracking(self, matrix, mark, rows, cols, row, col, path, pathlen):
        if pathlen == len(path):
            return True
        next_search = False
        if row >= 0 and row <rows and col >= 0 and col < cols and matrix[row][col] == path[pathlen] and mark[row][col] == False:
            pathlen += 1
            matrix[row][col] = True
            next_search = self.backtracking(matrix, mark, rows, cols, row-1, col, path, pathlen) or self.backtracking(matrix, mark, rows, cols, row+1, col, path, pathlen) or self.backtracking(matrix, mark, rows, cols, row, col-1, path, pathlen) or self.backtracking(matrix, mark, rows, cols, row, col+1, path, pathlen) 
            if not next_search:
                pathlen -= 1
                mark[row][col] = False
        return next_search


def main():
	s = Solution()
	matrix = "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
	path = "SGGFIECVAASABCEHJIGQEM"
	rows = 5
	cols = 8
	print(s.hasPath(matrix, rows, cols, path))

if __name__ == '__main__':
	main()
