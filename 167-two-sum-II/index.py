from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1

        sum = numbers[index1] + numbers[index2]
        while sum != target:
            if sum < target:
                index1 += 1
            else:
                index2 -= 1
            sum = numbers[index1] + numbers[index2]

        return [index1 + 1, index2 + 1]



def twoSum(numbers, target):
    print('**************************')
    print(numbers)
    solution = Solution()
    result = solution.twoSum(numbers, target)
    print(result)
    return result

assert twoSum([2,7,11,15], 9) == [1,2], 'First'
assert twoSum([2,3,4], 6) == [1,3], 'Second'
assert twoSum([-1,0], -1) == [1,2], 'Third'
