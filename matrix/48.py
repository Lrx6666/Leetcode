##48 旋转图像
import copy
from copy import deepcopy


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        tmp = deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                matrix[j][n - i - 1] = tmp[i][j]

##感觉矩阵的题还挺背板的，记住原地算法用深拷贝这个库deepcopy
##i j 的规律记住{行换列，列合n}