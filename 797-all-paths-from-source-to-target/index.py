# backtracking dfs dag

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        allPaths = []
        path = [0]

        def backtrack(node):
            for nextNode in graph[node]:
                path.append(nextNode)
                backtrack(nextNode)
                if nextNode == len(graph) - 1:
                    allPaths.append(path.copy())
                path.pop()

        backtrack(0)

        return allPaths

def allPathsSourceTarget(graph: List[List[int]]) -> bool:
    print('**************************')
    print(graph)
    solution = Solution()
    result = solution.allPathsSourceTarget(graph)
    print(result)
    return result

assert allPathsSourceTarget([
    [1,2],
    [3],
    [3],
    []
]) == [[0,1,3],[0,2,3]], 'First'

assert allPathsSourceTarget([
    [4,3,1],
    [3,2,4],
    [3],
    [4],
    []
]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], 'Second'

assert allPathsSourceTarget([
    [1,3,4,5],
    [2,5],
    [3,4,5],
    [5],
    [],
    []
]) == [[0,1,2,3,5],[0,1,2,5],[0,1,5],[0,3,5],[0,5]], 'Third'