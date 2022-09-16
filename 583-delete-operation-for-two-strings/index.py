# dynamicprogramming string

# Step 1: calculate longest common subsequence
# Step 2: calculate number of charater need to delete
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # +1 col to handle case j = 0
        prevRowDp = [0] * (len(word2) + 1)

        for i in range(len(word1)):
            curRowDp = [0] * (len(word2) + 1)
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    curRowDp[j] = prevRowDp[j - 1] + 1
                else:
                    curRowDp[j] = max(curRowDp[j-1], prevRowDp[j])
            prevRowDp = curRowDp
        
        return len(word1) + len(word2) - curRowDp[-2] * 2

def minDistance(word1: str, word2: str) -> int:
    print('***************************')
    print(word1, word2)
    sls = Solution()
    result = sls.minDistance(word1, word2)
    print('--------------')
    print(result)
    return result

assert minDistance("sea", "eat") == 2
assert minDistance("leetcode", "etco") == 4