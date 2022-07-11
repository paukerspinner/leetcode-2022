from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowSize, colSize = len(grid), len(grid[0])

        directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        
        roots = []
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 2:
                    roots.append((row, col))

        time = 0
        while len(roots) > 0:
            newRoots = []
            for (row, col) in roots:
                for (dx, dy) in directions:
                    adjRow = row + dx
                    adjCol = col + dy
                    if 0 <= adjRow < rowSize and 0 <= adjCol < colSize and grid[adjRow][adjCol] == 1:
                        newRoots.append((adjRow, adjCol))
                        grid[adjRow][adjCol] = 2
            if len(newRoots) > 0:
                time += 1
            roots = newRoots

        for row in grid:
            for elem in row:
                if elem == 1:
                    return -1

        return time

def orangesRotting(grid):
    sls = Solution()
    print('**********************')
    for row in grid:
        print(row)
    result = sls.orangesRotting(grid)
    print(result)
    return result

assert orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4, 'First'
assert orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1, 'Second'
assert orangesRotting([[0,2]]) == 0, 'Third'
assert orangesRotting([[2]]) == 0, 'Only one orange, it is rotten'
assert orangesRotting([[2,1]]) == 1, 'One rotten, one fresh'
assert orangesRotting([[2,0],[0,1]]), 'One rotten, no fresh is the next of rotten'
assert orangesRotting([[2,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,0,1,1,2]]) == 6, 'Complex input'