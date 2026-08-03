##73矩阵置零
class Solution:
    def setZeroes(self , matrix: List[List[int]]) -> None:
        self.rows , self.cols = len(matrix), len(matrix[0])
        def modify( x , y ):
            for i in range(self.rows):
                if matrix[i][y] != 0:
                    matrix[i][y] = 'm'
            for j in range(self.cols):
                if matrix[x][j] != 0:
                    matrix[x][j] = 'm'

        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == 0:
                    modify(i , j)
        for i in range(self.rows):
            for j in range(self.cols):
                if matrix[i][j] == 'm':
                    matrix[i][j] = 0
        return
