'''机器人的运动范围：
	地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标
的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
请问该机器人能够达到多少个格子？'''
'''使用深度优先搜索（Depth First Search，DFS）方法进行求解。
回溯是深度优先搜索的一种特例，它在一次搜索过程中需要设置一些本次搜索过程
的局部状态，并在本次搜索结束之后清除状态。而普通的深度优先搜索并不需要使
用这些局部状态，虽然还是有可能设置一些全局状态。'''
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        self.cnt = 0 # 用于格子得计数
        self.th = threshold
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)] # 用于保存每个格子对应得计数和
        self.mark = [[False for _ in range(cols)] for _ in range(rows)] # 用于标记一个格子是否已经进入
        self.helper(rows, cols) # 用于计算一个格子对应的数字
        self.dfs(rows, cols, 0, 0) # 深度优先遍历
        return self.cnt
    
    def helper(self, rows, cols):
        res = [0] * max(rows, cols)
        for i in range(len(res)):
            while i > 0:
                res[i] += i%10
                i //= 10
        
        for i in range(rows):
            for j in range(cols):
                self.matrix[i][j] = res[i] + res[j]
                
    def dfs(self, rows, cols, row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols or self.mark[row][col]:
            return
        self.mark[row][col] = True
        if self.matrix[row][col] > self.th:
            return 
        self.cnt += 1
        self.dfs(rows, cols, row+1, col)
        self.dfs(rows, cols, row-1, col)
        self.dfs(rows, cols, row, col+1)
        self.dfs(rows, cols, row, col-1)
def main():
	s = Solution()
	print(s.movingCount(15, 20, 20))

if __name__ == "__main__":
	main()
