from advent2020.day3.puzzle_map import PuzzleMap


class Route:
    def __init__(self, path: str) -> None:
        self._map = PuzzleMap(path)

    def toboggan_run(self, x_step: int, y_step: int) -> int:
        trees_encountered = 0
        x = 0
        for y in range(0, self._map.y_size, y_step):
            if self._map.is_tree(x, y):
                trees_encountered += 1
            x += x_step
        return trees_encountered
