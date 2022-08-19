# dynamic-programming

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        canJumpFromList = [None] * length

        def canJumpFrom(pos: int):
            print(pos)
            if length - pos - 1 <= nums[pos]:
                return True
            else:
                for step in range(nums[pos], 0, -1):
                    if canJumpFromList[pos + step] == None:
                        canJumpFromList[pos + step] = canJumpFrom(pos + step) 
                    if canJumpFromList[pos + step] == True:
                        return True
                return False
        
        return canJumpFrom(0)

def canJump(nums: List[int]) -> bool:
    print('***************************')
    print(nums)
    sls = Solution()
    result = sls.canJump(nums)
    print('--------------')
    print(result)
    return result

assert canJump([2,3,1,1,4]) == True, 'First'
assert canJump([3,2,1,0,4]) == False, 'Second'
assert canJump([0]) == True, 'Third'
assert canJump([1,3,1,0,0,1,5]) ==  False, 'Fourth'
assert canJump([1,4,1,0,0,1,5]) ==  True, 'Fifth'
assert canJump([5,3,1,0,0,1,5]) ==  True, 'Sixth'
assert canJump([2,0,0]) == True, 'Seventh'
assert canJump([8,5,1,4,5,2,3,6,5,1,1,2,5,8,5,2,9,2,4,4,5,2,2,1,2,5,2,2]) == True, 'Eighth'