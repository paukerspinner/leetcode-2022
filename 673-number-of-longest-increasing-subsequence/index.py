# dynamicprogramming
from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lenLISList = [None] * len(nums)
        countList = [None] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            maxLenOfChild = 0
            count = 1
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    if lenLISList[i] == maxLenOfChild:
                        count += countList[i]
                    if lenLISList[i] > maxLenOfChild:
                        maxLenOfChild = lenLISList[i]
                        count = countList[i]
            lenLISList[idx] = 1 + maxLenOfChild
            countList[idx] = count
        res = 0
        for i, elem in enumerate(lenLISList):
            if elem == max(lenLISList):
                res += countList[i]
        return res

def findNumberOfLIS(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.findNumberOfLIS(nums)
    print('--------------')
    print(result)
    return result

assert findNumberOfLIS([1,3,5,4,7]) == 2
assert findNumberOfLIS([10,9,2,5,3,7,101,18]) == 4
assert findNumberOfLIS([0,1,0,3,2,3]) == 1
assert findNumberOfLIS([7,7,7,7,7,7,7]) == 7
assert findNumberOfLIS([1,3,5,4,7]) == 2
assert findNumberOfLIS([2,2,2,2]) == 4