class Order:
    def __init__(self, busses: str) -> None:
        self._busses = [(index, int(x)) for index, x in enumerate(busses.split(','))
                        if x != 'x']

    def find_sequence_start_time(self) -> int:
        pass
