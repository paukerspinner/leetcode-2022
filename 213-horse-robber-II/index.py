# dynamic-programming

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        thirdPrev = secondPrev = firstPrev = 0
        thirdPrevWithoutFirst = secondPrevWithoutFirst = firstPrevWithoutFirst = 0
        robMax = 0

        for idx, elem in enumerate(nums):
            maxPrev = max(thirdPrev, secondPrev) if idx != len(nums) - 1 else max(thirdPrevWithoutFirst, secondPrevWithoutFirst)
            cur = elem + maxPrev

            curWithoutFirst = 0 if idx == 0 else elem + max(thirdPrevWithoutFirst, secondPrevWithoutFirst)

            thirdPrev, secondPrev, firstPrev = secondPrev, firstPrev, cur
            thirdPrevWithoutFirst, secondPrevWithoutFirst, firstPrevWithoutFirst = secondPrevWithoutFirst, firstPrevWithoutFirst, curWithoutFirst

            robMax = max(robMax, cur)

        return robMax

def rob(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.rob(nums)
    print('--------------')
    print(result)
    return result

assert rob([2,3,2]) == 3, 'First'
assert rob([1,2,3,1]) == 4, 'Second'
assert rob([1,2,3]) == 3, 'Third'
assert rob([5,3,1,2,0,3]) == 8, 'Fourth'