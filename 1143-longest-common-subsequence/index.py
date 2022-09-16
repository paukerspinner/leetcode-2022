# dynamicprogramming string
from typing import List

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]    # +1 row and +1 col to handle case i = 0 or j = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[-2][-2]

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