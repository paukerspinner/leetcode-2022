from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pCount = [0] * 26
        for c in p:
            pCount[ord(c) - ord('a')] += 1
        
        sSubCount = [0] * 26
        for i, c in enumerate(s):
            start = i - len(p) + 1
            if start > 0:
                sSubCount[ord(s[start - 1]) - ord('a')] -= 1
            sSubCount[ord(c) - ord('a')] += 1
            if sSubCount == pCount:
                res.append(start)

        return res

def findAnagrams(s: str, p: str) -> List[int]:
    print('**************************')
    print(s)
    solution = Solution()
    result = solution.findAnagrams(s, p)
    print(result)
    return result

assert findAnagrams("cbaebabacd", "abc") == [0,6], 'First'
assert findAnagrams("abab", "ab") == [0,1,2], 'Second'
assert findAnagrams("abccbacbca", "abc") == [0,3,4,5,7], 'Third'