from advent2020.day5.seat_identifier import SeatIdentifier
from advent2020.utils.read_file import ReadFile


class SeatAllocations:
    def __init__(self, path: str) -> None:
        self._seats = [SeatIdentifier(id) for id in ReadFile.lines(path)]

    def find_max_occupied(self) -> int:
        return max([seat.id for seat in self._seats])

    def find_empty_seat(self) -> int:
        id = [seat.id for seat in self._seats]
        start = min(id)
        stop = max(id)
        for seat in range(start, stop):
            if seat not in id:
                return seat
        raise ValueError("Seat not found")
