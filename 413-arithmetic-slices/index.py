# dynamic-programming arithmetic slices

from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        prevDiff = -1e9
        start, end = 0, 1
        while end < len(nums):
            diff = nums[end] - nums[end - 1]
            if diff != prevDiff:
                start = end - 1
                prevDiff = diff
            else:
                res += end - start - 1
            end += 1

        return res

def numberOfArithmeticSlices(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.numberOfArithmeticSlices(nums)
    print('--------------')
    print(result)
    return result

assert numberOfArithmeticSlices([1,2,3,4]) == 3, 'First'
assert numberOfArithmeticSlices([1]) == 0, 'Second'
assert numberOfArithmeticSlices([1,2,3,4,5,7,9,11,12,13]) == 10, 'Third'
assert numberOfArithmeticSlices([0,0,0]) == 1, 'Fourth'
assert numberOfArithmeticSlices([3,3,3,2,2,2,1,1,1]) == 3, 'Fifth'
assert numberOfArithmeticSlices([3,2,1,0,-1]) == 6, 'Sixth'