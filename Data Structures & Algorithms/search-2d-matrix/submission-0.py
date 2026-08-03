class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                return self.binSearch(matrix[m], target)
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False

    def binSearch(self, arr: List[int], target: int) -> bool:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l+r) // 2
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
