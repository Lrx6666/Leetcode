## 54 螺旋矩阵
class Solution:
    def spiralOrder(self , matrix : List[List[int]]) -> List[int]:
        if not matrix :
            return []
        t = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        res = []

        while True:
            for i in range(l , r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b : break
            for i in range(t , b+1):
                res.append(matrix[i][r])
            r -= 1
            if r < t : break
            for i in range(r , l-1 , -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b: break
            for i in range(b , t-1 , -1):
                res.append(matrix[i][l])
            l += 1
            if r < t: break
        return res

#我理解的是到第三步已经横纵都收缩过一次了所以 i 的range要变成l-1 t-1
#range里面的-1是步长
#边界判断的思路是走完哪条边 判断与对边的关系