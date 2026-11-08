class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row, target):
            l, r = 0, len(row) - 1

            while l <= r:
                mid = (l + r) // 2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    l += 1
                else:
                    r -= 1
            
            return False
        
        for row in matrix:
            if binarySearch(row, target):
                return True
        return False