# dynamic programming greedy
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLenTo = []
        
        for i in range(len(nums)):
            prevMax = 0
            for j in range(len(maxLenTo)):
                if nums[i] > nums[j]:
                    prevMax = max(prevMax, maxLenTo[j])
            maxLenTo.append(prevMax + 1)

        return max(maxLenTo)

def lengthOfLIS(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.lengthOfLIS(nums)
    print('--------------')
    print(result)
    return result

assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
assert lengthOfLIS([0,1,0,3,2,3]) == 4
assert lengthOfLIS([7,7,7,7,7,7,7]) == 1

def lengthOfLIS(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.lengthOfLIS(nums)
    print('--------------')
    print(result)
    return result

assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
assert lengthOfLIS([0,1,0,3,2,3]) == 4
assert lengthOfLIS([7,7,7,7,7,7,7]) == 1