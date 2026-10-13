class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        m = 0 
        n = c - 1
        while r > m and n >= 0:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] < target:
                m +=1
            else:
                n -= 1
        return False
            