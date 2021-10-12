from advent2020.day13.order import Order
from advent2020.day13.timetable import Timetable
from advent2020.utils.read_file import ReadFile


class ShuttleBus:
    def __init__(self, path: str) -> None:
        input = ReadFile.lines(path)
        self._start_time = int(input[0])
        self._busses = input[1]

    def puzzle_1(self) -> int:
        sut = Timetable(self._busses)
        bus, time = sut.find_next_bus(self._start_time)
        return bus * time

    def puzzle_2(self) -> int:
        sut = Order(self._busses)
        return sut.find_sequence_start_time()
