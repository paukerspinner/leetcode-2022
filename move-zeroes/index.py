from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        next = 0
        while next < len(nums):
            if nums[next] != 0:
                nums[index], nums[next] = nums[next], nums[index]
                index += 1
            next += 1
        
        return nums


def moveZeroes(nums):
    print('************************')
    print(nums)
    solution = Solution()
    result = solution.moveZeroes(nums)
    print(result)
    return result


assert moveZeroes([0,1,0,3,12]) == [1,3,12,0,0], 'First'
assert moveZeroes([0]) == [0], 'Second'
assert moveZeroes([1,2,3,0,0,0]) == [1,2,3,0,0,0], 'No any moving'
assert moveZeroes([0,0,1,0,0,0,2,0,0,0,1,0,0]) == [1,2,1,0,0,0,0,0,0,0,0,0,0], 'Complex input'