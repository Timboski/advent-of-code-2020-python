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
        if not isinstance(other, Layout):
            return False

        if self.y_size != other.y_size:
            return False

        for i in range(self.y_size):
            if self._state[i] != other._state[i]:
                return False

        return True

    def occupied_seat_count(self) -> int:
        return sum([row.count('#') for row in self._state])

    def simulate_round(self) -> Layout:
        return Layout([self._simulate_row(y) for y in range(self.y_size)])

    def _simulate_row(self, y: int) -> str:
        return "".join([self._simulate_cell(x, y) for x in range(self.x_size)])

    def _simulate_cell(self, x: int, y: int) -> str:
        start_state = self._state[y][x]
        if start_state == '.':
            return '.'  # No seat (remains not a seat)
        occupied = self._num_occupied_neighbours(x, y)
        if start_state == 'L':
            # Empty seat - becomes occupied if no adjacent seats occupied.
            return '#' if occupied == 0 else 'L'
        if start_state == '#':
            # Occupied seat - becomes empty if 4 or more adjacent seats occupied.
            return 'L' if occupied >= 4 else '#'
        raise ValueError("Unexpected seat state")

    def _num_occupied_neighbours(self, x: int, y: int) -> int:
        offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        return sum([1 for xo, yo in offsets if self._cell_occupied(x + xo, y + yo)])

    def _cell_occupied(self, x: int, y: int) -> bool:
        if (x < 0) or (y < 0) or (x >= self.x_size) or (y >= self.y_size):
            return False
        return self._state[y][x] == '#'
