from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []

        idx1 = idx2 = 0
        left = right = 0
        while idx1 < len(firstList) and idx2 < len(secondList):
            left = max(firstList[idx1][0], secondList[idx2][0])
            right = min(firstList[idx1][1], secondList[idx2][1])
            if left <= right:
                res.append([left, right])
            if firstList[idx1][1] < secondList[idx2][1]:
                idx1 += 1
            else:
                idx2 += 1

        return res


def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) ->  List[List[int]]:
    print('***************************')
    print(firstList)
    print(secondList)
    sls = Solution()
    result = sls.intervalIntersection(firstList, secondList)
    print('--------------')
    print(result)
    return result


assert intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]], 'First'
assert intervalIntersection([[1,3],[5,9]], []) == [], 'Second'
assert intervalIntersection([[3,4],[6,9]], [[4,6],[9,10]]) == [[4,4],[6,6],[9,9]], 'Third'
assert intervalIntersection([[3,10]], [[4,5],[6,8],[9,10]]) == [[4,5],[6,8],[9,10]], 'Fourth'
assert intervalIntersection([[3,5]], [[5,10]]) == [[5,5]], 'Fifth'