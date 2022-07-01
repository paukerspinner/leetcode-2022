# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(n: int) -> bool:
    return True
class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(0, n)
    
    def binarySearch(self, left, right):
        mid = (left + right) >> 1
        if isBadVersion(mid):
            return mid if not isBadVersion(mid - 1) else self.binarySearch(left, mid - 1)
        else:
            return self.binarySearch(mid + 1, right)