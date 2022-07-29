from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxS = 0

        while left != right:
            area = min(height[left], height[right]) * (right - left)
            if area > maxS:
                maxS = area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxS

def maxArea(height: List[int]) -> int:
    print('**************************')
    print(height)
    solution = Solution()
    result = solution.maxArea(height)
    print(result)
    return result

assert maxArea([1,8,6,2,5,4,8,3,7]) == 49, 'First'
assert maxArea([1,1]) == 1, 'Second'
assert maxArea([1,8,6,2,5,4,8,3,6]) == 42, 'Third'
assert maxArea([1,8,6,100,88,4,8,3,7,10]) == 88, 'Fourth'
assert maxArea([8,6,3,10,10,3,6,8]) == 56, 'Fifth'
assert maxArea([0,0,0,0,0,0,0,0,1]) == 0, 'Sixth'
assert maxArea([1,8,6,2,5,4,8,3,3]) == 40, 'Seventh'