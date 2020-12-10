from advent2020.day3.puzzle_map import PuzzleMap


class Route:
    def __init__(self, path: str) -> None:
        self._map = PuzzleMap(path)

    def toboggan_run(self) -> int:
        trees_encountered = 0
        x = 0
        for y in range(self._map.y_size):
            if self._map.is_tree(x, y):
                trees_encountered += 1
            x += 3
        return trees_encountered
