from advent2020.utils.read_file import ReadFile


class Haversacks:
    def __init__(self, path: str) -> None:
        self._rules = ReadFile.lines(path)

    def num_colour_options(self) -> int:
        pass
