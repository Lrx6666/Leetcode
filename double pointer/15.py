##15 三数之和为0
class Solution:
    def threeSum (self , nums : List[int]) -> List[List[int]]:
        nums.sort()
        res , k = [] , 0
        for k in range(len(nums) - 2) : #k最大只能到倒数第三个数
            if nums[k] > 0 : break #第一个都大于0 了绝对没有符合条件的数组
            if k > 0 and nums[k] == nums[k-1] : continue #重复，剪枝
            i , j = k + 1 , len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0 :
                    i+=1
                    while i < j and nums[i] == nums[i-1]: i+=1 #去重 可以不写 仅仅加速剪枝
                elif s > 0 :
                    j-=1
                    while i < j and nums[j] == nums[j+1]: j-=1 
                else:
                    res.append([nums[k] , nums[i] , nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i-1]: i+=1 #核心去重
                    while i < j and nums[j] == nums[j+1]: j-=1
        return res