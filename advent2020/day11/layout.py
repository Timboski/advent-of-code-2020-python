from __future__ import annotations

from typing import List, Tuple

from advent2020.utils.read_file import ReadFile


class Layout:
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    def __init__(self, state: List[str], alternate_strategy: bool = False) -> None:
        self._state = state
        self.x_size = len(state[0])
        self.y_size = len(state)
        self._alternate_strategy = alternate_strategy
        self._seat_threshold = 5 if alternate_strategy else 4
        self._num_occupied_neighbours = (self._num_occupied_neighbours_visible
                                         if alternate_strategy else
                                         self._num_occupied_neighbours_adjacent)

    @staticmethod
    def from_file(path: str, *, alternate_strategy: bool = False) -> Layout:
        return Layout(ReadFile.lines(path), alternate_strategy)

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
        return Layout([self._simulate_row(y) for y in range(self.y_size)],
                      alternate_strategy=self._alternate_strategy)

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
            # Occupied seat - becomes empty if adjacent occupied seats hits threshold.
            return 'L' if occupied >= self._seat_threshold else '#'
        raise ValueError("Unexpected seat state")

    def _num_occupied_neighbours_adjacent(self, x: int, y: int) -> int:
        return sum(
            [1 for xo, yo in self.offsets if self._cell_occupied(x + xo, y + yo)])

    def _cell_occupied(self, x: int, y: int) -> bool:
        if self._cell_out_of_range(x, y):
            return False
        return self._state[y][x] == '#'

    def _num_occupied_neighbours_visible(self, x: int, y: int) -> int:
        return sum([1 for offset in self.offsets if self._cell_visible(x, y, offset)])

    def _cell_visible(self, x: int, y: int, offset: Tuple[int]) -> bool:
        xo, yo = offset
        while True:
            x += xo
            y += yo
            if self._cell_out_of_range(x, y):
                return False  # Reached edge of layout - no occupied seat seen

            seat_state = self._state[y][x]
            if seat_state == '#':
                return True  # Occupied seat spotted
            if seat_state == 'L':
                return False  # Empty seat spotted

            # No seat seen - loop again moving in the same direction
            # (Check that this is an empty floor space)
            if seat_state != '.':
                raise ValueError("Unexpected seat state")

    def _cell_out_of_range(self, x: int, y: int) -> bool:
        return (x < 0) or (y < 0) or (x >= self.x_size) or (y >= self.y_size)
