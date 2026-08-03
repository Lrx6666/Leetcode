##240 搜索二维矩阵
class Solution:
    def searchMatrix(self , matrix : List[List[int]] , target : int) -> bool :
        i = len(matrix) - 1
        j = 0
        while i>=0 and j < len(matrix[0]): #此处第二个不能取等否则内存越界
            if matrix[i][j] < target : j+=1
            elif matrix[i][j] > target : i-=1
            else : return True
        return False

##神之思路不得不跪下来膜拜，应该能记一辈子
##代码写法上while里面三个条件是互斥的所以用if elif else不能改
##target的判断从左下角的根节点开始，初始i j 赋值要类数组从0开始
##至于if elif里面怎么删减行画个图自己想想就行
