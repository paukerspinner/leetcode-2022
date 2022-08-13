# backtracking permute permutation unique duplicate

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        allPermutations = []

        def backtrack(selects: List[int], remains: List[int]):
            if not remains:
                allPermutations.append(selects)
                return
            prevSelect = None
            for idx in range(len(remains)):
                if remains[idx] != prevSelect:
                    backtrack(selects + [remains[idx]], remains[:idx] + remains[idx + 1:])
                prevSelect = remains[idx]

        backtrack([], nums)

        return allPermutations

def permuteUnique(nums: List[int]):
    print('***********************')
    print(nums)
    sls = Solution()
    result = sls.permuteUnique(nums)
    print('------------')
    print(result)
    return result

assert permuteUnique([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], 'First'
assert permuteUnique([0,1]) == [[0,1],[1,0]], 'Second'
assert permuteUnique([1]) == [[1]], 'Third'
assert permuteUnique([1,1]) == [[1,1]], 'Fourth'
assert permuteUnique([1,1,2,2]) == [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]], 'Sixth'
assert permuteUnique([1,1,2]) == [[1,1,2],[1,2,1],[2,1,1]], 'Fifth'
assert permuteUnique([1,2,1,2]) == [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]], 'Seventh'
