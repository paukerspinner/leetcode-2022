from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minTotals = [[] for row in triangle]

        for i, row in enumerate(triangle):
            for j, elem in enumerate(row):
                print(i,j)
                if i == j == 0:
                    minTotals[i].append(elem)
                elif j == 0:
                    minTotals[i].append(minTotals[i-1][j] + elem)
                elif j == len(row) - 1:
                    minTotals[i].append(minTotals[i-1][j-1] + elem)
                else:
                    minTotals[i].append(min(minTotals[i-1][j-1], minTotals[i-1][j]) + elem)
        
        for row in minTotals:
            print(row)
        
        return min(minTotals[-1])


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