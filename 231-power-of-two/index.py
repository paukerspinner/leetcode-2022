class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binLen = len(bin(n)[2:])
        return n ^ 2**(binLen - 1) == 0


def isPowerOfTwo(n: int) -> int:
    print('***************************')
    print(n)
    sls = Solution()
    result = sls.isPowerOfTwo(n)
    print('--------------')
    print(result)
    return result

assert isPowerOfTwo(1) == True, 'First True'
assert isPowerOfTwo(2) == True, 'Second True'
assert isPowerOfTwo(4) == True, 'Third True'
assert isPowerOfTwo(8) == True, 'Fourth True'
assert isPowerOfTwo(16) == True, 'Fifth True'
assert isPowerOfTwo(1024) == True, 'Sixth True'
assert isPowerOfTwo(3) == False, 'First False'
assert isPowerOfTwo(5) == False, 'Second False'
assert isPowerOfTwo(15) == False, 'Third False'
assert isPowerOfTwo(9) == False, 'Fourth False'
assert isPowerOfTwo(18) == False, 'Fifth False'
assert isPowerOfTwo(255) == False, 'Sixth False'