from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) >> 1
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                left = right = mid
            elif nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left

def findPeakElement(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.findPeakElement(nums)
    print('--------------')
    print(result)
    return result

assert findPeakElement([1,2,3,1]) == 2, 'First'
assert findPeakElement([1,2,1,3,5,6,4]) == 5, 'Second'
assert findPeakElement([0,1,2,3,4,3,2,5,2,9]) in [4,7,9], 'Third'
assert findPeakElement([9,8,7,8,2,0,1,4,6,3]) in [0,3,8], 'Fourth'
assert findPeakElement([5,3,2,1,0]) == 0, 'Found at the first, descreasing list'
assert findPeakElement([4,5,6,7,8,9]) == 5, 'Found at the end, ascending list'
assert findPeakElement([5]) == 0, 'One elem'
assert findPeakElement([2,2]) in [0,1], 'Two equal elemments'
assert findPeakElement([3,3,3,3,3]) in [0,4], 'Five equal elements'
assert findPeakElement([1,2]) == 1, 'Two ascending list'
assert findPeakElement([5,4]) == 0, 'Two descending list'