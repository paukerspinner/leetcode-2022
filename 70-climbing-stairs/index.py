class Solution:
    def climbStairs(self, n: int) -> int:
        stepCount = []
        idx = 0
        while idx <= n:
            if idx <= 3:
                count = idx
            else:
                count = stepCount[idx-1] + stepCount[idx-2]
            stepCount.append(count)

            idx += 1
        
        return stepCount[-1]

def climbStairs(n: int):
    print('***********************')
    print(n)
    sls = Solution()
    result = sls.climbStairs(n)
    print('------------')
    print(result)
    return result

assert climbStairs(2) == 2, 'First'
assert climbStairs(3) == 3, 'Second'
assert climbStairs(5) == 8, 'Third'