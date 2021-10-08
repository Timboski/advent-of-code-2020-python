from __future__ import annotations

from advent2020.utils.read_file import ReadFile


class Layout:
    def __init__(self, path: str) -> None:
        self._start = ReadFile.lines(path)

    def is_same_state(self, other: Layout) -> bool:
        pass

    def simulate_round(self) -> Layout:
        pass
