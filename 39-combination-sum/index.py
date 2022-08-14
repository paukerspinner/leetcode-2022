
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(selections: List[int], sum: int, candidates: List[int]):
            if sum == target:
                res.append(selections)
                return
            for nextIdx, nextElem in enumerate(candidates):
                nextSum = sum + nextElem
                if nextSum > target:
                    break
                backtrack(selections + [nextElem], nextSum, candidates[nextIdx:])

        backtrack([], 0, candidates)

        return res

def combinationSum(candidates: List[int], target: int):
    print('***********************')
    print(candidates, target)
    sls = Solution()
    result = sls.combinationSum(candidates, target)
    print('------------')
    print(result)
    return result

assert combinationSum([2,3,6,7], 7) == [[2,2,3],[7]], 'First'
assert combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]], 'Second'
assert combinationSum([2], 1) == [], 'Third'
assert combinationSum([2,5,3], 8) == [[2,2,2,2],[2,3,3],[3,5]], 'Fourth'
assert combinationSum([1,2,3], 6) == [[1,1,1,1,1,1],[1,1,1,1,2],[1,1,1,3],[1,1,2,2],[1,2,3],[2,2,2],[3,3]]
