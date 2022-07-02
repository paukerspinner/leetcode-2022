from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

def reverseString(s):
    solution = Solution()
    result = solution.reverseString(s)
    return result

assert reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"], 'First'
assert reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"], 'Second'
