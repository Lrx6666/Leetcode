## 283 移动0
##数组 双指针

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 :
                nums[left] , nums[right] = nums[right] , nums[left]
                left += 1

#range()取数组下标

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        n = len(nums)
        #设置左右指针，还有列表长度
        while right < n:
            #小于（最大下标+1）就是取所有下标，这是边界判断
            if nums[right] != 0:
                nums[left] , nums[right] = nums[right] , nums[left]
                #交换位置
                left += 1
                #加上
            right += 1
            #每一次都加上
        return nums
        #返回

for right in range(len(nums)):
和
right = 0

while right < len(nums):
    xxxxx
    right += 1
是一个意思，range更简洁