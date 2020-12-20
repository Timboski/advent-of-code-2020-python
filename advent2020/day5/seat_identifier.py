class SeatIdentifier:
    def __init__(self, seat_id: str) -> None:
        self._id = seat_id.replace("F", "0")
        self._id = self._id.replace("B", "1")
        self._id = self._id.replace("L", "0")
        self._id = self._id.replace("R", "1")

    @property
    def row(self) -> int:
        return int(self._id[0:7], 2)

    @property
    def column(self) -> int:
        return int(self._id[7:10], 2)

    @property
    def id(self) -> int:
        return int(self._id, 2)
