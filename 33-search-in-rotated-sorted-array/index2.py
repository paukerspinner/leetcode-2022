from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minIdx = self.findIndexOfMin(nums)
        idxInSortedArray = self.binarySearch(nums[minIdx:] + nums[:minIdx], target)
        print(minIdx, idxInSortedArray)
        return -1 if idxInSortedArray == -1 else (minIdx + idxInSortedArray) % len(nums)
    
    def binarySearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) >> 1
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left if nums[left] == target else -1

    def findIndexOfMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) >> 1
            if nums[left] <= nums[mid] <= nums[right]:
                right = left
            elif nums[right] < nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left

def search(nums: List[int], target: int) -> int:
    print('***************************')
    print(nums, target)
    sls = Solution()
    result = sls.search(nums, target)
    print('--------------')
    print(result)
    return result

assert search([4,5,6,7,0,1,2], 0) == 4, 'Simple found'
assert search([4,5,6,7,0,1,2], 3) == -1, 'Simple not found'
assert search([1], 0) == -1, 'One elem, not found'
assert search([1], 1) == 0, 'One elem, found'
assert search([4,5,6,1,2], 2) == 4, 'found at last, odd number of element'
assert search([4,5,6,7,1,2], 2) == 5, 'found at last, even number of element'
assert search([5,6,8,9,10,11,4], 5) == 0, 'found at first, odd number of element'
assert search([8,9,1,2,3,4], 8) == 0, 'found at first, even number of element'
assert search([1,2,3,4,5,6,7,8,9,10], 5) == 4, 'found at first, even number of element, ascending array'
assert search([1,2,3,4,5,6,7,8,9], 9) == 8, 'found at first, odd number of element, ascending array'
assert search([8,9,10,11,12,13], 3) == -1, 'not found, smaller than the smallest, even number of element, ascending array'
assert search([8,9,10,11,12], 3) == -1, 'not found, smaller than the smallest, odd number of element, ascending array'
assert search([8,9,10,11,12,15], 18) == -1, 'not found, bigger than the biggest, even number of element, ascending array'
assert search([8,9,10,11,12], 18) == -1, 'not found, bigger than the biggest, odd number of element, ascending array'
assert search([4,5,6,7,8,1,2,3], 8) == 4, 'found at biggest'
assert search([5,1,2,3,4], 1) == 1, 'found at smallest'
