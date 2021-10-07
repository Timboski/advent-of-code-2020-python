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

    def find_weakness(self, first_invalid: int):
        for i in range(len(self._data)):
            sum_range = self._find_sum_range(i, first_invalid)
            if sum_range is not None:
                return Decoder._sum_min_max(sum_range)
        raise ValueError("No encryption weakness found")

    def _is_solution(current: int, history: List[int]):
        for i in history:
            remainder = current - i
            if (remainder != i) and (remainder in history):
                return True
        return False

    def _find_sum_range(self, start_index: int, target: int) -> List[int]:
        acc = 0
        for i in range(start_index, len(self._data), 1):
            acc += self._data[i]
            if acc == target:
                return self._data[start_index:i + 1]
            if acc > target:
                return None
        return None

    def _sum_min_max(sum_range: List[int]) -> int:
        return min(sum_range) + max(sum_range)
