from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) >> 1
            if nums[left] <= nums[mid] <= nums[right]:
                right = left
            elif nums[right] < nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]

def findMin(nums: List[int]) -> int:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.findMin(nums)
    print('--------------')
    print(result)
    return result

assert findMin([3,4,5,1,2]) == 1, 'Found, rotated 3 times'
assert findMin([3,4,5,6,1,2]) == 1, 'Found, rotated 4 times'
assert findMin([3,4,5,0]) == 0, 'Found at last, rotated 3 times, even number of elements'
assert findMin([3,4,5,6,2]) == 2, 'Found, rotated 4 times, odd number of elements'
assert findMin([0,1,2,3,4,5]) == 0, 'Found, not rotated, event number of elements'
assert findMin([0,1,2,3,4]) == 0, 'Found, not rotated, odd number of elements'