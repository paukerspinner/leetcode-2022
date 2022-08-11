from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rowSize, colSize = len(board), len(board[0])
        queue = []

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(rowSize):
            if board[i][0] == 'O':
                queue.append((i,0))
                board[i][0] = 'F'
            if board[i][colSize-1] == 'O':
                queue.append((i,colSize - 1))
                board[i][colSize - 1] = 'F'
    
        for j in range(colSize):
            if board[0][j] == 'O':
                queue.append((0,j))
                board[0][j] = 'F'
            if board[rowSize - 1][j] == 'O':
                queue.append((rowSize - 1, j))
                board[rowSize - 1][j] = 'F'


        while queue:
            curi, curj = queue.pop(0)
            for di, dj in directions:
                i = curi + di
                j = curj + dj
                if 0 <= i < rowSize and 0 <= j < colSize and board[i][j] == 'O':
                    queue.append((i,j))
                    board[i][j] = 'F'

        for i in range(rowSize):
            for j in range(colSize):
                if board[i][j] == 'F':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        return board

def solve(board: List[List[str]]):
    sls = Solution()
    print('**********************')
    for row in board:
        print(row)
    result = sls.solve(board)
    print('----------------------')
    print(result)
    return result

assert solve([
    ['X','X','X','X'],
    ['X','O','O','X'],
    ['X','X','O','X'],
    ['X','O','X','X']
]) == [
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['X','O','X','X']
], 'First'

assert solve([
    ['X']
]) ==[
    ['X']
], 'Second'

assert solve([
    ['X','X','X'],
    ['X','O','X'],
    ['X','O','X'],
    ['X','X','X'],
    ['X','O','X'],
    ['X','O','X'],
    ['X','O','O']
]) == [
    ['X','X','X'],
    ['X','X','X'],
    ['X','X','X'],
    ['X','X','X'],
    ['X','O','X'],
    ['X','O','X'],
    ['X','O','O']
], 'Third'