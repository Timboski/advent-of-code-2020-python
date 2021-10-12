from advent2020.day11.layout import Layout


class SeatingSimulation:
    def __init__(self, path: str, *, alternate_strategy: bool = False) -> None:
        self._start = Layout.from_file(path, alternate_strategy=alternate_strategy)

    def occupied_seat_count(self) -> int:
        current = self._start
        previous = None
        while not current.is_same_state(previous):
            previous = current
            current = current.simulate_round()
        return current.occupied_seat_count()
