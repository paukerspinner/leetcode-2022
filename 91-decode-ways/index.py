# dynamic-programming decode

from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        numdict = {}
        
        def calc(s):
            if s == '':
                return 1

            if s in numdict.keys():
                return numdict[s]
            case1 = calc(s[2:]) if len(s) >= 2 and '09' < s[0:2] <= '26' else 0
            case2 = calc(s[1:]) if len(s) >= 1 and int(s[0]) > 0 else 0
            numdict[s] = case1 + case2
            return numdict[s]
        return calc(s)

def numDecodings(s: str) -> int:
    print('***************************')
    print(s)
    sls = Solution()
    result = sls.numDecodings(s)
    print('--------------')
    print(result)
    return result

assert numDecodings("12") == 2, 'First'
assert numDecodings("226") == 3, 'Second'
assert numDecodings("06") == 0, 'Third'
assert numDecodings("11106") == 2, 'Fourth'
assert numDecodings("111111111111111111111111111111111111111111111") == 1836311903, 'Fifth'