from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(perm: str, remain: str):
            if not remain:
                res.append(perm)
                return
            
            chr = remain[0]
            backtrack(perm + chr, remain[1:])
            if chr >= 'a' and chr <= 'z':
                backtrack(perm + chr.upper(), remain[1:])
            if chr >= 'A' and chr <= 'Z':
                backtrack(perm + chr.lower(), remain[1:])
            
        backtrack("", s)

        return res

def letterCasePermutation(s: str):
    print('***********************')
    print(s)
    sls = Solution()
    result = sls.letterCasePermutation(s)
    print('------------')
    print(result)
    return result

assert letterCasePermutation("a1b2") == ["a1b2","a1B2","A1b2","A1B2"], 'First'
assert letterCasePermutation("3z4") == ["3z4","3Z4"], 'Second'
assert letterCasePermutation(["z"]) == ["z","Z"], 'Third'