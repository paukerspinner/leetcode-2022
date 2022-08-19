# dynamic-programming

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(1, m):
            curRow = []
            for j in range(n):
                if j == 0:
                    curRow.append(1)
                else:
                    curRow.append(curRow[-1] + row[j])
            row = curRow

        return row[-1]

def uniquePaths(m: int, n: int) -> int:
    print('***************************')
    print(m, n)
    sls = Solution()
    result = sls.uniquePaths(m, n)
    print('--------------')
    print(result)
    return result

assert uniquePaths(3,7) == 28, 'First'
assert uniquePaths(3,2) == 3, 'Second'
assert uniquePaths(12,6)