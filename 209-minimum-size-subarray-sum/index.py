from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        res = 1e9 + 1
        left = right = 0
        while right < len(nums):
            if sum < target:
                sum += nums[right]
            else:
                sum -= nums[left - 1]
            
            if sum < target:
                right += 1
            else:
                if right - left + 1 < res:
                    res = right - left + 1
                left += 1
                if right < left:
                    right = left
                    sum = 0
        return res if res != 1e9 + 1 else 0

def minSubArrayLen(target: int, nums: List[int]) -> int:
    print('***********************************')
    print(nums, target)
    sls = Solution()
    result = sls.minSubArrayLen(target, nums)
    print('-----------------------')
    print(result)
    return result

assert minSubArrayLen(7, [2,3,2,2,4,3]) == 2, 'First'
assert minSubArrayLen(4, [1,4,4]) == 1, 'Second'
assert minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0, 'Third'
assert minSubArrayLen(8, [2,6,5,4,7,8,2,1,4,6]) == 1, 'Fourth'
assert minSubArrayLen(8, [8]) == 1, 'Fifth'
assert minSubArrayLen(8, [0]) == 0, 'Sixth'
assert minSubArrayLen(24, [1,3,5,6,2,4,7,8,9]) == 3, 'Seventh'
assert minSubArrayLen(35, [2,5,6,4,1,0,1,8,2,5,1]) == 11, 'Eighth'
assert minSubArrayLen(11, [1,2,3,4,5]) == 3, 'Nineth'