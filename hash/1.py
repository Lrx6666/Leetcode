#两数之和 哈希
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}#定义一个字典{键，值}

        for i, num in enumerate(nums):#调用enumerate遍历数组
            complement = target - num#计算当前num对应的补值complement
            if complement in num_to_index: #如果补值在字典里
                return [num_to_index[complement], i]  #返回complement对应的i和当前i
            num_to_index[num] = i #把当前数字存进去

        return []
#测试例
if __name__ == "__main__":
    sol = Solution()

    result1 = sol.twoSum([2, 7, 11, 15],13)
    print(result1)
