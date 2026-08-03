class Solution:
    def searchMatrix(self , matrix : List[List[int]] , target : int) -> bool :
        i = len(matrix) - 1
        j = len(matrix[0]) - 1
        while i>=0 and j <=len(matrix[0]):
            if matrix[i][j] < target : j++
            if matrix[i][j] > target : i--
            if matrix[i][j] == target : return True
            else : return False