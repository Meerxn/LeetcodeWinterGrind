class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower = 0
        upper = len(matrix) -1
        found_row = False
        while lower <= upper:
            middle = (upper + lower) // 2
            if target > matrix[middle][-1]:
                lower = middle + 1
            elif target < matrix[middle][0]:
                upper = middle -1
            else:
                found_row = True
                break
        if found_row == False:
            return False
        print(middle,lower,upper)
        left = 0
        right = len(matrix[0])
        while(left <=right):
            m = (left+right) // 2
            if target > matrix[middle][m]:
                left = m + 1
            elif target < matrix[middle][m]:
                right = m - 1
            else:
                return True
        return False
                
                