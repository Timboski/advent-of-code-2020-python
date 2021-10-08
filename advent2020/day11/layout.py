from __future__ import annotations

from typing import List

from advent2020.utils.read_file import ReadFile


class Layout:
    def __init__(self, state: List[str]) -> None:
        self._state = state
        self.x_size = len(state[0])
        self.y_size = len(state)

    @staticmethod
    def from_file(path: str) -> Layout:
        return Layout(ReadFile.lines(path))

    def is_same_state(self, other: Layout) -> bool:
        if self.y_size != other.y_size:
            return False

        for i in range(self.y_size):
            if self._state[i] != other._state[i]:
                return False

        return True

    def occupied_seat_count(self) -> int:
        return sum([row.count('#') for row in self._state])

    def simulate_round(self) -> Layout:
        pass
