from json.tool import main
from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums: List[int], left: int, right: int, target: int):

        if left == right:
            return left if nums[left] == target else -1
        
        mid = (left + right) >> 1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)
        if nums[mid] > target:
            return self.binarySearch(nums, left, right - 1, target)

def search(nums: List[int], target: int) -> int:
    solution = Solution()
    result = solution.search(nums, target)
    return result

assert search([-1,0,3,5,9,12], 9) == 4, 'First found'
assert search([-1,0,3,5,9,12], 2) == -1, 'First not found'
assert search([1,2,3,4,5], 5) == 4, 'Found last index'
assert search([-1,0,3,5,9,12], -1) == 0, 'Found first index'
assert search([1], 1) == 0, 'Found one element'
assert search([1], 0) == -1, 'Not found one element'
assert search([1,2], 3) == -1, 'Not found exceed max'
assert search([-1,0,3,5,9,12], -5), 'Not found exceed min'

