# dynamic-programming palindromic substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l = r = i
            if i - 1 >= 0 and s[i] == s[i - 1]:
                l = i - 1
                r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l - 1 > len(res):
                res = s[l + 1: r]

            if i - 2 >= 0 and s[i] == s[i - 2]:
                l = i - 2
                r = i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l - 1 > len(res):
                res = s[l + 1: r]

        return res

def longestPalindrome(s: str) -> str:
    print('***************************')
    print(s)
    sls = Solution()
    result = sls.longestPalindrome(s)
    print('--------------')
    print(result)
    return result

assert longestPalindrome("babad") == "bab", 'First'
assert longestPalindrome("cbbd") == "bb", 'Second'
assert longestPalindrome("babab") == "babab", 'Third'
assert longestPalindrome("accbbcaaab") == "cbbc", 'Fourth'
assert longestPalindrome("cc") == "cc", 'Fifth'
assert longestPalindrome("lllllllllllll") == "lllllllllllll", 'Sixth'
assert longestPalindrome("x") == "x", 'Sixth'

