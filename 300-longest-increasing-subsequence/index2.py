# dynamic programming greedy
from typing import List
class Solution:
    def binarySearch(self, nums: List[int], target: int):
        if len(nums) == 0 or target > nums[-1]:
            return -1
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        increasingList = []
        for elem in nums:
            pos = self.binarySearch(increasingList, elem)
            if pos == -1:
                increasingList.append(elem)
            else:
                increasingList[pos] = elem
        return len(increasingList)

def lengthOfLIS(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.lengthOfLIS(nums)
    print('--------------')
    print(result)
    return result

def binarySearch(nums: List[int], target: int):
    print('***************************')
    print(nums, target)
    sls = Solution()
    result = sls.binarySearch(nums, target)
    print('--------------')
    print(result)
    return result


assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
assert lengthOfLIS([0,1,0,3,2,3]) == 4
assert lengthOfLIS([7,7,7,7,7,7,7]) == 1