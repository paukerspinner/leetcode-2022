from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prevRowMinTotals = [0]
        for row in triangle:
            rowMinTotals = []
            for j, elem in enumerate(row):
                if j == 0:
                    prevMinTotal = prevRowMinTotals[j]
                elif j == len(row) - 1:
                    prevMinTotal = prevRowMinTotals[j-1]
                else:
                    prevMinTotal = min(prevRowMinTotals[j-1], prevRowMinTotals[j])
                rowMinTotals.append(prevMinTotal + elem)
            prevRowMinTotals = rowMinTotals
        
        return min(rowMinTotals)


def minimumTotal(triangle: List[List[int]]) -> int:
    print('***************************')
    for row in triangle:
        print(row)
    sls = Solution()
    result = sls.minimumTotal(triangle)
    print('--------------')
    print(result)
    return result

assert minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]) == 11, 'First'
assert minimumTotal([[-10]]) == -10, 'Second'
assert minimumTotal([[2],[3,3]]) == 5, 'Third'
assert minimumTotal([[2],[3,4],[6,5,1]]) == 7, 'Fourth'
assert minimumTotal([[7],[-5,9],[6,5,2],[-8,-2,-7,3],[-2,6,-6,-1,4]]) == -6, 'Fifth'