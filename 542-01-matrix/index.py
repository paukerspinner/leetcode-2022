from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowNum, colNum = len(mat), len(mat[0])
        rootQueue = []
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        for row in range(rowNum):
            for col in range(colNum):
                if mat[row][col] == 0:
                    rootQueue.append([0, (row, col)])
                else:
                    mat[row][col] = None
        
        while(len(rootQueue) > 0):
            val, (row, col) = rootQueue.pop(0)
            for (dx, dy) in directions:
                adjRow = row + dx
                adjCol = col + dy
                if 0 <= adjRow < rowNum and 0 <= adjCol < colNum and mat[adjRow][adjCol] is None:
                    mat[adjRow][adjCol] = adjVal = val + 1
                    rootQueue.append([adjVal, (adjRow, adjCol)])
        
        return mat

def updateMatrix(mat):
    sls = Solution()
    print('****************************')
    for row in mat:
        print(row, end='\n')
    
    result = sls.updateMatrix(mat)
    print('--------------')
    for row in result:
        print(row, end='\n')
    return result

assert updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == [[0,0,0],[0,1,0],[0,0,0]], 'First'
assert updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]], 'Second'
assert updateMatrix([[0,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,1,1,0,1,1,0],[1,1,1,1,1,1,1]]) == [[0,0,1,0,1,0,1],[1,0,1,1,1,0,1],[2,1,1,0,1,1,0],[3,2,2,1,2,2,1]], 'Third'
assert updateMatrix([[1,1,1,1,1,1,0,1,1,1],[1,1,0,0,0,0,0,1,1,1],[0,1,0,1,1,1,1,0,0,0],[1,1,1,0,0,1,1,0,1,1],[1,0,1,1,1,0,1,1,1,1],[1,1,0,0,1,0,1,1,1,1],[1,0,1,0,0,0,1,1,0,1],[1,1,0,1,1,1,1,0,0,1],[1,1,1,1,0,0,0,1,1,0],[1,1,1,0,1,1,0,1,1,1]]) == [[2,2,1,1,1,1,0,1,2,2],[1,1,0,0,0,0,0,1,1,1],[0,1,0,1,1,1,1,0,0,0],[1,1,1,0,0,1,1,0,1,1],[1,0,1,1,1,0,1,1,2,2],[2,1,0,0,1,0,1,2,1,2],[1,0,1,0,0,0,1,1,0,1],[2,1,0,1,1,1,1,0,0,1],[3,2,1,1,0,0,0,1,1,0],[3,2,1,0,1,1,0,1,2,1]], 'Fourth'