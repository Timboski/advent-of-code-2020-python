class SeatIdentifier:
    def __init__(self, seat_id: str) -> None:
        self._row = seat_id.replace("F", "0")
        self._row = self._row.replace("B", "1")
        self._row = self._row[0:7]

        self._column = seat_id.replace("L", "0")
        self._column = self._column.replace("R", "1")
        self._column = self._column[7:10]

    @property
    def row(self) -> int:
        return int(self._row, 2)

    @property
    def column(self) -> int:
        return int(self._column, 2)
