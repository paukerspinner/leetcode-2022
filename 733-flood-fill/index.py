from time import sleep
from typing import List

class Solution:
    def __init__(self) -> None:
        self.visited = dict()
        self.initialColor = None

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.initialColor = image[sr][sc] if not self.initialColor else self.initialColor
        image[sr][sc] = color
        if f"{sr}, {sc}" in self.visited.keys():
            return
        else:
            self.visited[f"{sr}, {sc}"] = True

        if sr - 1 >= 0 and image[sr - 1][sc] == self.initialColor:
            self.floodFill(image, sr - 1, sc, color)
        if sc - 1 >= 0 and image[sr][sc - 1] == self.initialColor:
            self.floodFill(image, sr, sc - 1, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == self.initialColor:
            self.floodFill(image, sr + 1, sc, color)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == self.initialColor:
            self.floodFill(image, sr, sc + 1, color)

        return image


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    print('***********************************')
    for row in image:
        print(row)
    print(sr, sc, color)
    sls = Solution()
    result = sls.floodFill(image, sr, sc, color)
    print('-----------------------')
    for row in result:
        print(row)
    return result

assert floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]], 'First'
assert floodFill([[0,0,0],[0,0,0]], 0, 0, 0) == [[0,0,0],[0,0,0]], 'Second'