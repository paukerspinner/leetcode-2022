from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provNum, cityNum = 0, len(isConnected)
        isVisited = [False] * cityNum
        def dfs(i):
            if isVisited[i] == True:
                return
            isVisited[i] = True
            for j in range(cityNum):
                if isConnected[i][j] == 1:
                    dfs(j)

        for i in range(cityNum):
            if not isVisited[i]:
                provNum += 1
                dfs(i)
        
        return provNum


def findCircleNum(isConnected: List[List[int]]) -> int:
    print('***********************************')
    for row in isConnected:
        print(row)
    sls = Solution()
    result = sls.findCircleNum(isConnected)
    print('-----------------------')
    print(result)
    return result

assert findCircleNum([
    [1,1,0],
    [1,1,0],
    [0,0,1]
]) == 2, 'First'

assert findCircleNum([
    [1,0,0],
    [0,1,0],
    [0,0,1]
]) == 3, 'Second'

assert findCircleNum([
    [1,1,0,0,1,1],
    [1,1,0,0,0,0],
    [0,0,1,0,1,1],
    [0,0,0,1,0,1],
    [1,0,1,0,1,0],
    [1,0,1,1,0,1]
]) == 1, 'third'

assert findCircleNum([
    [1,0,0,0,0],
    [0,1,1,1,1],
    [0,1,1,0,1],
    [0,1,0,1,0],
    [0,1,0,0,1]
]) == 2, 'Fourth'