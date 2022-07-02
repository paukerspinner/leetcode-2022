from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
    
    def binarySearch(self, nums, left, right, target):
        if left == right:
            if target <= nums[left]:
                return left
            else:
                return left + 1
        
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, mid + 1, right, target)
        else:
            return self.binarySearch(nums, left, right - 1, target)

def searchInsert(nums: List[int], target: int) -> int:
    solution = Solution()
    return solution.searchInsert(nums, target)

assert searchInsert([1,3,5,6], 5) == 2, 'First'
assert searchInsert([1,3,5,6], 2) == 1, 'Second'
assert searchInsert([1,3,5,6], 7,) == 4, 'Third'
assert searchInsert([1,3,5,6], 0) == 0, 'Less than min'
assert searchInsert([1], 2) == 1, 'Greater than max, one element'
assert searchInsert([1], 0) == 0, 'Less than min, one element'