from typing import Tuple


class Timetable:
    def __init__(self, busses: str) -> None:
        self._busses = [int(x) for x in busses.split(',') if x != 'x']

    def find_next_bus(self, time: int) -> Tuple[int, int]:
        next_times = [self._next_time(bus, time) for bus in self._busses]
        index_min = min(range(len(next_times)), key=next_times.__getitem__)
        return self._busses[index_min], next_times[index_min]

    @staticmethod
    def _next_time(bus: int, time: int):
        time_into_journey = time % bus
        return bus - time_into_journey
