class Solution:
    def hammingWeight(self, n: int) -> int:
        print(n, bin(n))
        if n == 0:
            return 0
        return (n & 1) + self.hammingWeight(n >> 1)

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