from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        maxLen = 0
        for c in s:
            indexOfChar = substr.find(c)
            if indexOfChar == -1:
                substr += c
            else:
                substr = substr[indexOfChar+1:] + c
            maxLen = max(maxLen, len(substr))
        return maxLen

def lengthOfLongestSubstring(s):
    print('*************************************')
    solution = Solution()
    print(s)
    result = solution.lengthOfLongestSubstring(s)
    print(result)
    return result

assert lengthOfLongestSubstring("abcabcbb") == 3, 'First'
assert lengthOfLongestSubstring("bbbbb") == 1, 'Second'
assert lengthOfLongestSubstring("pwwkew") == 3, 'Third'
assert lengthOfLongestSubstring('abc') == 3, 'unique characters'
assert lengthOfLongestSubstring("abcababcbca") == 3, 'Complex input'
assert lengthOfLongestSubstring('') == 0, 'Empty string'
assert lengthOfLongestSubstring('abcabcd') == 4, 'Longest at the end'