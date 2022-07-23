from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        while left != right:
            mid = (left + right) >> 1
            if target <= nums[mid]:
                right = mid
            elif nums[mid] < target:
                left = mid + 1

        if nums[left] != target:
            return [-1,-1]
        

        firstPos = left
        left, right = firstPos, len(nums) - 1

        while left != right:
            mid = (left + right + 1) >> 1
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid] or (target == nums[mid] and mid + 1 < len(nums) and target == nums[mid + 1]):
                left = mid + 1
            else:
                left = mid
            
        lastPos = left if nums[left] == target else -1

        return [firstPos, lastPos]

def searchRange(nums: List[int], target: int) -> int:
    print('***************************')
    print(nums, target)
    sls = Solution()
    result = sls.searchRange(nums, target)
    print('--------------')
    print(result)
    return result

assert searchRange([5,7,7,8,8,10], 8) == [3,4], 'First 6 elems'
assert searchRange([5,7,8,8,10], 8) == [2,3], 'First 5 elems'
assert searchRange([5,7,7,8,8,10], 6) == [-1,-1], 'Second'
assert searchRange([], 0) == [-1,-1], 'Third'
assert searchRange([1,2,3,3,3,3,3,3,3,4],3) == [2, 8], 'Fourth'
assert searchRange([1,2,3,3,3,3,3,3,3,3,4],3) == [2,9], 'Fifth'
assert searchRange([1], 1) == [0,0], 'Only 1 element and found'
assert searchRange([1], 0) == [-1,-1], 'Only 1 element and not found'
assert searchRange([1,2,3,4,5], 5) == [4,4], 'Found at the end'
assert searchRange([0,1,1,1,1,2,2,2,3,3,3,3,4,5,6,6,8,9,9,9], 0) == [0,0], 'Found 1 at first'