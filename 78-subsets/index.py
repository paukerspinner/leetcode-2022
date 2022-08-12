# backtracking subset

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = [[]]

        for num in nums:
            newSubsets = []
            for subset in allSubsets:
                newSubsets.append(subset + [num])
            
            allSubsets += newSubsets

        return allSubsets

def subsets(nums: List[int]) -> List[List[int]]:
    print('**************************')
    print(nums)
    solution = Solution()
    result = solution.subsets(nums)
    print(result)
    return result

assert subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], 'First'
assert subsets([0]) == [[],[0]], 'Second'
assert subsets([0,1]) == [[], [0], [1], [0,1]], 'Third'
assert subsets([1,2,3,4]) == [
    [],
    [1],
    [2],[1,2],
    [3],[1,3],[2,3],[1,2,3],
    [4],[1,4],[2,4],[1,2,4],[3,4],[1,3,4],[2,3,4],[1,2,3,4],
], 'Fourth'