from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1st = prev2nd = prev3rd = 0
        for elem in nums:
            maxRob = max(prev3rd, prev2nd) + elem
            prev3rd, prev2nd, prev1st = prev2nd, prev1st, maxRob 

        return max(prev2nd, prev1st)


def rob(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.rob(nums)
    print('--------------')
    print(result)
    return result

assert rob([1,2,3,1]) == 4, 'First'
assert rob([2,7,9,3,1]) == 12, 'Second'
assert rob([0]) == 0, 'Only one element'
assert rob([1,2]) == 2, 'Two element, second bigger than first'
assert rob([2,1]) == 2, 'Two element, first bigger than second'
assert rob([2,7,9,10,1]) == 17, 'Complex 1'
assert rob([2,17,9,1,2]) == 19, 'Complex 2'