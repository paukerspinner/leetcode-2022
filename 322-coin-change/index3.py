# dynamicprogramming bottom up
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        dp = [0] + [MAX] * amount
        for i in range(amount + 1):
            for coin in coins:
                key = i - coin
                if key >= 0:
                    dp[i] = min(dp[i], 1 + dp[key])
        return dp[-1] if dp[-1] != MAX else -1

def coinChange(coins: List[int], amount: int) -> int:
    print('***************************')
    print(coins, amount)
    sls = Solution()
    result = sls.coinChange(coins, amount)
    print('--------------')
    print(result)
    return result

assert coinChange([1,2,5], 11) == 3
assert coinChange([2], 3) == -1
assert coinChange([1], 0) == 0
assert coinChange([1,2,3,4,5], 26) == 6
assert coinChange([1,3,7,10], 65) == 8
assert coinChange([2,5,6,8], 84) == 11
assert coinChange([2,5,10,1], 27) == 4
assert coinChange([4,5,11,17], 18) == 4
assert coinChange([1,5,11], 15) == 3