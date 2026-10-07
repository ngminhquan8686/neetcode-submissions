class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_idx = -1

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            mid_row = top + (bottom - top) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else: 
                row_idx = mid_row
                break
        if row_idx == -1:
            return False

        left , right = 0, COLS - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix[mid_row][mid]:
                left = mid + 1
            elif target < matrix[mid_row][mid]:
                right = mid - 1
            else:
                return True
        
        return False
            
        
            
        
        