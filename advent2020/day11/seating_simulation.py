from advent2020.utils.read_file import ReadFile


class SeatingSimulation:
    def __init__(self, path: str) -> None:
        self._start = ReadFile.lines(path)

    def occupied_seat_count(self) -> int:
        pass
