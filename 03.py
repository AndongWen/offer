'''在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的
   ，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复
     的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个
    重复的数字2。'''
'''要求时间复杂度 O(N)，空间复杂度 O(1)。因此不能使用排序的方法，也不能使用额外的标记数组。

对于这种数组元素在 [0, n-1] 范围内的问题，可以将值为 i 的元素调整到第 i 个位置上进行求解。

以 (2, 3, 1, 0, 2, 5) 为例，遍历到位置 4 时，该位置上的数为 2，但是第 2 个位置上已经有一个 2 的值了，因此可以知道 2 重复'''

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    temp = numbers[i]
                    numbers[i] = numbers[numbers[i]]
                    numbers[numbers[i]] = temp
        return False
