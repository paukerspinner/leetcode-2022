# backtracking

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowSize, colSize = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        isVisited = [[False] * colSize for row in board]

        def backtrack(i, j, word):
            if board[i][j] == word[0]:
                if len(word) == 1:
                    return True
                isVisited[i][j] = True
                for di, dj in directions:
                    nexti, nextj = i + di, j + dj
                    if 0 <= nexti < rowSize and 0 <= nextj < colSize and not isVisited[nexti][nextj]:
                        existWord = backtrack(nexti, nextj, word[1:])
                        if existWord:
                            return True
                        else:
                            isVisited[nexti][nextj] = False
            return False
        
        for i in range(rowSize):
            for j in range(colSize):
                isVisited = [[False] * colSize for row in board]
                res = backtrack(i, j, word)
                if res == True:
                    return True
        
        return False

def exist(board: List[List[str]], word: str) -> bool:
    print('**************************')
    for row in board:
        print(row)
    print(word)

    solution = Solution()
    result = solution.exist(board, word)
    print(result)
    return result

assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True, 'First'
assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True, 'Second'
assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False, 'Third'
assert exist([["A","B","C"],["S","F","C"],["A","D","E"]], "EDASFCCBA") == True, 'Fourth'
assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "FCSEEC") == False, 'Fifth'
assert exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS") == True, 'Sixth'