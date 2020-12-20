from advent2020.utils.read_file import ReadFile


class PuzzleMap:
    def __init__(self, path: str):
        lines = ReadFile.lines(path)
        self._trees = [[c == '#' for c in line] for line in lines]
        self._x_size = len(lines[0])
        self.y_size = len(lines)

    def is_tree(self, x: int, y: int) -> bool:
        if y >= self.y_size:
            raise ValueError(f"y ({y}) out of range. Size: {self.y_size}")
        wrapped_x = x % self._x_size
        return self._trees[y][wrapped_x]
