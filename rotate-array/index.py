from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tempnums = nums.copy()
        for i in range(len(nums)):
            nums[i] = tempnums[i-k]
        return nums
        
def rotate(nums, k):
    solution = Solution()
    result = solution.rotate(nums, k)
    return result

assert rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4], 'First'
assert rotate([-1,-100,3,99], 2) == [3,99,-1,-100], 'Second'
assert rotate([1,2,3,4,5], 15) == [1,2,3,4,5], 'In case k mod n == 0'