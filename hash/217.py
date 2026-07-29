#存在重复元素
#给数组 存在出现2次及以上的元素返回true

from typing import List
class Solution:
    def containDuplicate(self,nums : List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

#数字第一次出现：登记.add(num)
#数字第二次出现：发现已经登记过，说明重复，输出

#区分set()和set(nums)

#更简单的
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))