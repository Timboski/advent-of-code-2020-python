from advent2020.day5.seat_identifier import SeatIdentifier
from advent2020.utils.read_file import ReadFile


class SeatAllocations:
    def __init__(self, path: str) -> None:
        self._seats = [SeatIdentifier(id) for id in ReadFile.lines(path)]

    def find_max_occupied(self) -> int:
        return max([seat.id for seat in self._seats])
