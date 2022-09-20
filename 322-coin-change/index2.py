# dynamicprogramming dfs
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def getFewestNumberOfCoins(coins: List[int], amount: int) -> int:
            if amount == 0:
                return 0
            elif amount < 0:
                return None
            elif amount in dp.keys():
                return dp[amount]

            minNumberOfCoins = float('inf')
            for coin in coins:
                numOfcoins = getFewestNumberOfCoins(coins, amount - coin)
                if numOfcoins != None:
                    minNumberOfCoins = min(numOfcoins + 1, minNumberOfCoins)
            dp[amount] = minNumberOfCoins
            return minNumberOfCoins

        fewestNumberOfCoins = getFewestNumberOfCoins(coins, amount) 
        return fewestNumberOfCoins if fewestNumberOfCoins != float('inf') else -1

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