from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandNumber = 0
        rowSize, colSize = len(grid), len(grid[0])
        isVisited = [[0] * colSize for row in grid]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j):
            if grid[i][j] == '0' or isVisited[i][j] == 1:
                return

            isVisited[i][j] = 1
            for di, dj in directions:
                newi = i + di
                newj = j + dj
                if 0 <= newi < rowSize and 0 <= newj < colSize:
                    dfs(newi, newj)
        
        for i in range(rowSize):
            for j in range(colSize):
                if isVisited[i][j] == 0 and grid[i][j] == '1':
                    islandNumber += 1
                    dfs(i, j)

        return islandNumber

def numIslands(grid: List[List[int]]) -> int:
    print('***********************************')
    for row in grid:
        print(row)
    sls = Solution()
    result = sls.numIslands(grid)
    print('-----------------------')
    print(result)
    return result

assert numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1, 'First'
assert numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3, 'Second'
assert numIslands([
    ["1","1","1","1"],
    ["1","1","1","1"],
    ["1","1","1","1"],
]) == 1, 'Third'
assert numIslands([
    ["0","0","0","0"],
    ["0","0","0","0"],
    ["0","0","0","0"],
    ["0","0","0","0"],
    ["0","0","0","0"],
    ["0","0","0","0"],
    ["0","0","0","0"]
]) == 0, 'Fourth'
assert numIslands([
    ["1","0","1","0"],
    ["0","1","0","1"],
    ["1","0","1","0"],
    ["0","1","0","1"],
    ["1","0","1","0"],
    ["0","1","0","1"],
    ["1","0","1","0"]
]) == 14, 'Fifth'
assert numIslands([
    ["1","0","1","1"],
    ["1","0","1","0"],
    ["1","1","1","0"]
]) == 1, 'Sixth'