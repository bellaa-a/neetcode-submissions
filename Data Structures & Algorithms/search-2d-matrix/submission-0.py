class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        row = len(matrix)
        col = len(matrix[0])
        right = row*col-1

        while left <= right:
            m = left + int((right-left)/2)
            r = int(m/col)
            c = m % col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = m+1
            else:
                right = m-1
        
        return False