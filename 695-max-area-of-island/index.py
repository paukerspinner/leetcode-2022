from typing import List

class Solution:        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowNum, colNum = len(grid), len(grid[0])
        isVisited = [[False for i in grid[0]] for j in grid]
        maxS = 0

        def dfs(row, col):
            if isVisited[row][col] == True or grid[row][col] != 1:
                return 0
            else:
                isVisited[row][col] = True
            
            area = 1
            
            if row - 1 >= 0:
                area += dfs(row - 1, col)
            if row + 1 < rowNum:
                area += dfs(row + 1, col)
            if col - 1 >= 0:
                area += dfs(row, col - 1)
            if col + 1 < colNum:
                area += dfs(row, col + 1)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxS = max(dfs(i, j), maxS)

        return maxS

def maxAreaOfIsland(grid):
    sls = Solution()
    print('***************************')
    for row in grid:
        print(row)
    result = sls.maxAreaOfIsland(grid)
    print(result)
    return result

assert maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6, 'First'
assert maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0, 'One row full 0'
assert maxAreaOfIsland([[1,1,1,1,1]]) == 5, 'One row full 1'
assert maxAreaOfIsland([[1,1,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]) == 18, 'Full table 1'
assert maxAreaOfIsland([[1,0,1,0], [0,1,0,1], [1,0,1,0], [0,1,0,1]]) == 1, 'Like chessboard'