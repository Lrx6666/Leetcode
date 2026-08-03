##48 旋转图像
import copy
from copy import deepcopy


class Solution:
    def rotate(self , matrix : List[List[int]] -> None :
        n = len(matrix)
        tmp = deepcopy(matrix)

        for i in range(matrix):
            for j in range(matrix):
                matrix[j][n-i-1] = tmp[i][j]
