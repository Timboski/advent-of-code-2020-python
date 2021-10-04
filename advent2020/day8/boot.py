from advent2020.utils.read_file import ReadFile


class Boot:
    def __init__(self, path: str) -> None:
        self._code = ReadFile.lines(path)

    def find_acc_at_loop(self) -> int:
        pass
