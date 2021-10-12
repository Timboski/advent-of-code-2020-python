class Order:
    def __init__(self, busses: str) -> None:
        self._busses = [(index, int(x)) for index, x in enumerate(busses.split(','))
                        if x != 'x']

    def find_sequence_start_time(self) -> int:
        index_max_time = max(range(len(self._busses)),
                             key=[bus for _, bus in self._busses].__getitem__)
        index, step_size = self._busses[index_max_time]
        time = step_size - index
        while True:
            if self._test_sequence(time):
                return time
            time += step_size

    def _test_sequence(self, time: int) -> bool:
        for index, bus in self._busses:
            target = time + index
            if target % bus:
                return False
        return True
