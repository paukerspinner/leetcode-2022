class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = [0] * 26
        countS2 = [0] * 26

        for c in s1:
            countS1[ord(c) - ord('a')] += 1
        
        start = 0
        pos = 0

        while pos < len(s2):
            countS2[ord(s2[pos]) - ord('a')] += 1

            if pos - start + 1 == len(s1):
                if countS1 == countS2:
                    return True
                else:
                    countS2[ord(s2[start]) - ord('a')] -= 1
                    start += 1
            pos += 1

        return False
        

def checkInclusion(s1, s2):
    sls = Solution()
    result = sls.checkInclusion(s1, s2)
    return result

assert checkInclusion("ab", "eidbaooo") == True, 'First'
assert checkInclusion("ab", "eidboaoo") == False, 'Second'
assert checkInclusion("abc", "avvbbcbcbbcba") == True, 'Found at the end'
assert checkInclusion("abc", "cacanbcca") == False, 'Not found - lack one character'
assert checkInclusion("abd", "abbbabcddabcdacb") == True, 'Found'

