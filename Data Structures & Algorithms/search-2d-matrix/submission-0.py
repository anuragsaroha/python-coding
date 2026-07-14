class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        col = len(matrix[0])

        left = 0 
        right = rows

        while left < right:
            mid = (left + right)//2
            if matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid

        if left == rows:
            return False

        else:
            candidate_row = left
            left = 0 
            right = col
            while left < right:
                mid = (left + right)//2
                if matrix[candidate_row][mid] < target:
                    left = mid + 1
                else:
                    right = mid

            if left == col or matrix[candidate_row][left] != target:
                return False
            return True
            
        