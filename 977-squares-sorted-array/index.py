from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = len(nums) - 1
        while left < right:
            if abs(nums[left]) > abs(nums[right]):
                result += [nums[left] ** 2]
                left += 1
            else:
                result += [nums[right] ** 2]
                right -= 1

        return [nums[left] ** 2] + result[::-1]

def sortedSquares(nums):
    solution = Solution()
    result = solution.sortedSquares(nums)
    return result

assert sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100], 'First'
assert sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121], 'Second'
assert sortedSquares([-4]) == [16], 'One element'
assert sortedSquares([-2, -1]) == [1, 4], 'Two elements'
assert sortedSquares([1,2,3,4,5]) == [1,4,9,16,25], 'Only positive numbers'
assert sortedSquares([-5,-4,-3,-2,-1]), 'Only negative numbers'