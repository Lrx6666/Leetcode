##最长连续序列 哈希技巧应用

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
        return longest


nums = [100, 4, 200, 1, 2, 3]
print(Solution().longestConsecutive(nums))


## num_set = set(nums)
## set(nums)将定义的数组转换为集合
## 优点：1.去除重复的数字 2.后续判断一个数字是否在集合内O（1）
## 但是set()这样写就不去重只是创建空集合
##缩进问题：class定格 def一级 跳出循环的return和for一级 测试例定格写