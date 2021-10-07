from typing import List

from advent2020.utils.read_file import ReadFile


class Decoder:
    def __init__(self, path: str, preamble_length: int) -> None:
        self._len = preamble_length
        self._data = [int(i) for i in ReadFile.lines(path)]

    def find_first_invalid(self) -> int:
        for i in range(self._len, len(self._data), 1):
            history = self._data[i - self._len:i]
            current = self._data[i]
            if not Decoder._is_solution(current, history):
                return current
        raise ValueError("No invalid entry found")

    def _is_solution(current: int, history: List[int]):
        for i in history:
            remainder = current - i
            if (remainder != i) and (remainder in history):
                return True
        return False
