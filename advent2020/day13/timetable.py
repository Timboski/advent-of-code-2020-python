from typing import Tuple


class Timetable:
    def __init__(self, busses: str) -> None:
        self._busses = busses

    def find_next_bus(self, time: int) -> Tuple[int, int]:
        return 0, 0
