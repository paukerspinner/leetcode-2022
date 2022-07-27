from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, elem in enumerate(nums):
            if i > 0 and elem == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = elem + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([elem, nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1

        return res

def threeSum(nums: List[int]) -> List[List[int]]:
    print('**************************')
    print(nums)
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)
    return result

assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]], 'First'
assert threeSum([0,1,1]) == [], 'Second'
assert threeSum([0,0,0]) == [[0,0,0]], 'Third'
assert threeSum([3,0,-2,-1,1,2]) == [[-2,-1,3],[-2,0,2],[-1,0,1]], 'Fourth'
assert threeSum([0,0,0,0]) == [[0,0,0]], 'Fifth'