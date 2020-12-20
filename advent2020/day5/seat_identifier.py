class SeatIdentifier:
    def __init__(self, seat_id: str) -> None:
        self._row = seat_id.replace("F", "0")
        self._row = self._row.replace("B", "1")
        self._row = self._row[0:7]

    @property
    def row(self) -> int:
        return int(self._row, 2)
