# backtracking combination sum
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(selections: List[int], sum: int, remains: List[int]):
            if sum == target:
                res.append(selections)
                return
            prevSelection = None
            for idx, elem in enumerate(remains):
                nextSum = sum + elem
                if nextSum > target:
                    break
                if elem != prevSelection:
                    backtrack(selections + [elem], nextSum, remains[idx + 1:])
                    prevSelection = elem

        backtrack([], 0, candidates)
        return res

def combinationSum2(candidates: List[int], target: int):
    print('***********************')
    print(candidates, target)
    sls = Solution()
    result = sls.combinationSum2(candidates, target)
    print('------------')
    print(result)
    return result

assert combinationSum2([10,1,2,7,6,1,5], 8) == [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
], 'First'

assert combinationSum2([2,5,2,1,2], 5) == [
    [1,2,2],
    [5]
], 'Second'

assert combinationSum2([1], 1) == [[1]], 'Third'

assert combinationSum2([1], 2) == [], 'Fourth'

# assert combinationSum2([1], 0) == [], 'Fifth'
