from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color = image[sr][sc]
        changed = set()

        def col_change(x: int, y: int) -> None:
            if not 0 <= x < len(image) or not 0 <= y < len(image[0]) \
                    or image[x][y] != color or (x, y) in changed:
                return

            image[x][y] = newColor
            changed.add((x, y))

            col_change(x - 1, y)
            col_change(x + 1, y)
            col_change(x, y - 1)
            col_change(x, y + 1)

        col_change(sr, sc)
        return image
