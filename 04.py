'''给定一个二维数组，其每一行从左到右递增排序，从上到下也是递增排序。给定一个数，
	判断这个数是否在该二维数组中。'''

'''思路：要求时间复杂度 O(M + N)，空间复杂度 O(1)。其中 M 为行数，N 为 列数。

该二维数组中的一个数，小于它的数一定在其左边，大于它的数一定在其下边。
因此，从右上角开始查找，就可以根据 target 和当前元素的大小关系来缩小查找区间，
当前元素的查找区间为左下角的所有元素。每次判断可以减少一行或者一列'''


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array or len(array) == 0 or len(array[0]) == 0:
            return False
        x = len(array) 
        y = len(array[0])
        i, j = 0, y-1
        while i < x and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
