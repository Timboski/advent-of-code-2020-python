from __future__ import annotations

from typing import List

from advent2020.utils.read_file import ReadFile


class Layout:
    def __init__(self, state: List[str]) -> None:
        self._state = state

    @staticmethod
    def from_file(path: str) -> Layout:
        return Layout(ReadFile.lines(path))

    def is_same_state(self, other: Layout) -> bool:
        if len(self._state) != len(other._state):
            return False

        for i in range(len(self._state)):
            if self._state[i] != other._state[i]:
                return False

        return True

    def simulate_round(self) -> Layout:
        pass
