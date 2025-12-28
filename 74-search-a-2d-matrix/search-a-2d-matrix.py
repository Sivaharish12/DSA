class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        low, high = 0, rows - 1
        row_count = -1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][-1] >= target:
                row_count = mid
                high = mid - 1
            else:
                low = mid + 1

        if row_count == -1:
            return False

        low, high = 0, cols - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row_count][mid] == target:
                return True
            elif matrix[row_count][mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
