# backtracking combination

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        buttons = [ None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(selections: str, digitIdx: int):
            if len(selections) == len(digits):
                res.append(selections)
                return
            
            for ch in buttons[int(digits[digitIdx])]:
                backtrack(selections + ch, digitIdx + 1)

        if digits != "":
            backtrack("", 0)

        return res


def letterCombinations(digits: str) -> List[str]:
    print('***********************')
    print(digits)
    sls = Solution()
    result = sls.letterCombinations(digits)
    print('------------')
    print(result)
    return result

assert letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"], 'First'
assert letterCombinations("425") == [
    "gaj", "gak", "gal",
    "gbj", "gbk", "gbl",
    "gcj", "gck", "gcl",
    "haj", "hak", "hal",
    "hbj", "hbk", "hbl",
    "hcj", "hck", "hcl",
    "iaj", "iak", "ial",
    "ibj", "ibk", "ibl",
    "icj", "ick", "icl",
], 'Second'
assert letterCombinations("") == [], 'Third'
