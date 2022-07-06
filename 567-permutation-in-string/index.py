class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            if self.arePermutationsOfEachOther(s1, s2[i : i + len(s1)]):
                return True
        return False


    def arePermutationsOfEachOther(self, s1, s2):
        alphabetCountS1 = [0] * 26
        alphabetCountS2 = [0] * 26
        for c in s1:
            alphabetCountS1[ord(c) - ord('a')] += 1
        
        for c in s2:
            alphabetCountS2[ord(c) - ord('a')] += 1

        return alphabetCountS1 == alphabetCountS2



    def arePermutationsOfEachOther(self, s1, s2):
        alphabetCount = dict()
        for charCode in range(ord('a'), ord('z') + 1):
            alphabetCount[chr(charCode)] = 0
        for c in s1:
            alphabetCount[c] += 1
        
        for c in s2:
            alphabetCount[c] -= 1

        for c in alphabetCount.keys():
            if alphabetCount[c] != 0:
                return False
        
        return True
                
                

def checkInclusion(s1, s2):
    print('*****************************')
    print(s1, s2)
    sls = Solution()
    result = sls.checkInclusion(s1, s2)
    print(result)
    return result

assert checkInclusion("ab", "eidbaooo") == True, 'First'
assert checkInclusion("ab", "eidboaoo") == False, 'Second'
assert checkInclusion("abc", "avvbbcbcbbcba") == True, 'Found at the end'
assert checkInclusion("abc", "cacanbcca") == False, 'Not found - lack one character'