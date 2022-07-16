from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb: List[int]):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n):
                comb.append(i + 1)
                backtrack(i + 1, comb)
                comb.pop()

        backtrack(0, comb=[])

        return res 

def combine(n, k):
    sls = Solution()
    print('*************************')
    print(f"({n}, {k})")
    result = sls.combine(n, k)
    print(result)
    return result

assert len(combine(4, 2)) == 6, 'First'
assert len(combine(1,1)) == 1, 'Second'
assert len(combine(6, 3)) == 20, 'Third'