class Solution:
    def reverseBits(self, n: int) -> int:
        reverseN = 0
        for i in range(32):
            reverseN = (reverseN << 1) | (n & 1)
            n >>= 1
        return reverseN

def reverseBits(n: int) -> int:
    print('***************************')
    print(n)
    sls = Solution()
    result = sls.reverseBits(n)

    print('--------------')
    print(result)
    return result

assert reverseBits(43261596) == 964176192, 'First'
assert reverseBits(4294967293) == 3221225471, 'Second'
assert reverseBits(1) == 2147483648, 'One'
assert reverseBits(2) == 1073741824, 'Two'