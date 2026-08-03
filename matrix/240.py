##240 搜索二维矩阵
class Solution:
    def searchMatrix(self , matrix : List[List[int]] , target : int) -> bool :
        i = len(matrix) - 1
        j = 0
        while i>=0 and j < len(matrix[0]):
            if matrix[i][j] < target : j+=1
            elif matrix[i][j] > target : i-=1
            else : return True
        return False

##神之思路不得不跪下来膜拜，应该能记一辈子
##dai'm
