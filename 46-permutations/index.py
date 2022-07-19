from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm: List[int], remain: List[int]):
            if not remain:
                res.append(perm)
                return

            for idx, elem in enumerate(remain):
                backtrack(perm + [remain[idx]], remain[:idx] + remain[idx+1:])

        backtrack([], nums)

        return res

def permute(nums: List[int]):
    print('***********************')
    print(nums)
    sls = Solution()
    result = sls.permute(nums)
    print('------------')
    print(result)
    return result

assert permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], 'First'
assert permute([0,1]) == [[0,1],[1,0]], 'Second'
assert permute([1]) == [[1]], 'Third'