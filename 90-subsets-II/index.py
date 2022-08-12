# backtracking subset duplicate

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        allSubsets = [[]]
        lastAddedSubsets = []

        for idx, num in enumerate(nums):
            nextSubsets = []
            prevSubsets = allSubsets if num != nums[idx - 1] or idx == 0 else lastAddedSubsets
            for subset in prevSubsets:
                nextSubsets.append(subset + [num])
            allSubsets += nextSubsets
            lastAddedSubsets = nextSubsets.copy()

        return allSubsets

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    print('**************************')
    print(nums)
    solution = Solution()
    result = solution.subsetsWithDup(nums)
    print(result)
    return result

def isEqualList(list1, list2):
    if len(list1) != len(list2):
        return False
    for elem in list1:
        if elem not in list2:
            return False
    for elem in list2:
        if elem not in list1:
            return False
    return True

assert isEqualList(subsetsWithDup([1,2,3]), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]) == True, 'First'
assert isEqualList(subsetsWithDup([1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]]) == True, 'Second'
assert isEqualList(subsetsWithDup([0]), [[],[0]]) == True, 'Third'
assert isEqualList(subsetsWithDup([2,1,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]]) == True, 'Fourth'
