from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowSize, colSize = len(matrix), len(matrix[0])
        left, right = 0, rowSize * colSize - 1

        while left != right:
            mid = (left + right) >> 1
            
            if target > self.getElem(mid, matrix):
                left = mid + 1
            else:
                right = mid
        return self.getElem(left, matrix) == target
    
    def getElem(self, idx, matrix):
        i = idx // len(matrix[0])
        j = idx % len(matrix[0])
        return matrix[i][j]

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    print('***************************')
    for row in matrix:
        print(row)
    print(target)
    sls = Solution()
    result = sls.searchMatrix(matrix, target)
    print('--------------')
    print(result)
    return result

assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True, 'Found at first row'
assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False, 'Not found, value at middle'
assert searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 100) == False, 'Not found, bigger than the biggest'
assert searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 0) == False, 'Not found, smaller than the smallest'
assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60) == True, 'Found at last'
assert searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1) == True, 'Found at first'
