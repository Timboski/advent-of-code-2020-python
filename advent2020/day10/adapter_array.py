from advent2020.utils.read_file import ReadFile


class AdapterArray:
    def __init__(self, path: str) -> None:
        self._adapters = [int(i) for i in ReadFile.lines(path)]

    def find_sum(self) -> int:
        pass
