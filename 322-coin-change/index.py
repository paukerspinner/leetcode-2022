# dynamicprogramming
from typing import List

# getFewestNumberOfCoins = min(getFewestNumberOfCoins(coins[:-1], amount), getFewestNumberOfCoins(coins, amount - coins[-1]) + 1)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def getFewestNumberOfCoins(coins: List[int], amount: int) -> int:
            if (len(coins), amount) in dp.keys():
                return dp[(len(coins), amount)]
            if amount == 0:
                return 0
            elif amount < 0 or len(coins) == 0:
                return -1
            
            left = getFewestNumberOfCoins(coins[:-1], amount)
            right = getFewestNumberOfCoins(coins, amount - coins[-1])

            if left == -1 and right == -1:
                res = -1
            elif left != -1 and right != -1:
                res = min(right + 1, left)
            else:
                res = left if left != -1 else right + 1
            dp[(len(coins), amount)] = res
            return res

        return getFewestNumberOfCoins(coins, amount)

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