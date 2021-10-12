from advent2020.utils.read_file import ReadFile


class Course:
    def __init__(self, path: str) -> None:
        self._course = ReadFile.lines(path)

    def find_distance(self) -> int:
        pass
