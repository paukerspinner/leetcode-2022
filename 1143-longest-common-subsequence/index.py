# dynamicprogramming string
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # +1 col to handle case j = 0
        prevRowDp = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            curRowDp = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    curRowDp[j] = prevRowDp[j-1] + 1
                else:
                    curRowDp[j] = max(curRowDp[j-1], prevRowDp[j])
            prevRowDp = curRowDp
        return curRowDp[-2]

def longestCommonSubsequence(text1: str, text2: str) -> int:
    print('***************************')
    print(text1, text2)
    sls = Solution()
    result = sls.longestCommonSubsequence(text1, text2)
    print('--------------')
    print(result)
    return result

assert longestCommonSubsequence("abcde", "ace") == 3
assert longestCommonSubsequence("abc", "abc") == 3
assert longestCommonSubsequence("abc", "def") == 0
assert longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2