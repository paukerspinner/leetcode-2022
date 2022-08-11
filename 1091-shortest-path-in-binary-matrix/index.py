from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        matSize = len(grid)
        queue = [(0,0)]
        isVisited = [[False] * matSize for elem in grid]
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        else:
            grid[0][0] = 1
        
        while len(queue) > 0:
            curRow, curCol = queue.pop(0)
            isVisited[curRow][curCol] = True

            for dx, dy in directions:
                row = curRow + dx
                col = curCol + dy
                if 0 <= row < matSize and 0 <= col < matSize and grid[row][col] == 0 and not isVisited[row][col]:
                    grid[row][col] = grid[curRow][curCol] + 1
                    queue.append((row, col))              

        return grid[-1][-1] if grid[-1][-1] else -1

def shortestPathBinaryMatrix(grid: List[List[int]]):
    sls = Solution()
    print('**********************')
    for row in grid:
        print(row)
    result = sls.shortestPathBinaryMatrix(grid)
    print('----------------------')
    print(result)
    return result

assert shortestPathBinaryMatrix([
    [0,1],
    [1,0]
]) == 2, 'First'

assert shortestPathBinaryMatrix([
    [0,0,0],
    [1,1,0],
    [1,1,0]
]) == 4, 'Second'

assert shortestPathBinaryMatrix([
    [1,0,0],
    [1,1,0],
    [1,1,0]
]) == -1, 'Third'

assert shortestPathBinaryMatrix([
    [0,0,0],
    [0,1,1],
    [0,1,0]
]) == -1, 'Forth'

assert shortestPathBinaryMatrix([
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0],
    [1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
]) == 9, 'Fifth'