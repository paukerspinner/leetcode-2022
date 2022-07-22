from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res

def singleNumber(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.singleNumber(nums)
    print('--------------')
    print(result)
    return result

assert singleNumber([2,2,1]) == 1, 'First'
assert singleNumber([4,1,2,1,2]) == 4, 'Second'
assert singleNumber([1]) == 1, 'Third'
assert singleNumber([1,5,6,7,8,9,9,8,7,6,5,2,1]) == 2, 'Fourth'