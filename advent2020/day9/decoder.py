from advent2020.utils.read_file import ReadFile


class Decoder:
    def __init__(self, path: str, preamble_length: int) -> None:
        self._len = preamble_length
        self._data = [int(i) for i in ReadFile.lines(path)]

    def find_first_invalid(self) -> int:
        pass
