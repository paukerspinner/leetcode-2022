class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        while n > 0:
            hw += n & 1
            n >>= 1
        return hw

def hammingWeight(n: int) -> int:
    print('***************************')
    print(n)
    sls = Solution()
    result = sls.hammingWeight(n)
    print('--------------')
    print(result)
    return result

assert hammingWeight(11) == 3, 'First'
assert hammingWeight(128) == 1, 'Second'
assert hammingWeight(4294967293) == 31, 'Third'
assert hammingWeight(0) == 0, 'Zero'