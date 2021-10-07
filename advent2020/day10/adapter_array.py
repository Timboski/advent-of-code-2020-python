from advent2020.utils.read_file import ReadFile


class AdapterArray:
    def __init__(self, path: str) -> None:
        adapters = [int(i) for i in ReadFile.lines(path)]
        adapters.sort()

        device_jolts = adapters[-1] + 3
        self._joltages = [0] + adapters + [device_jolts]

    def find_sum(self) -> int:
        diffs = [
            self._joltages[i + 1] - self._joltages[i]
            for i in range(len(self._joltages) - 1)
        ]
        ones = diffs.count(1)
        threes = diffs.count(3)
        return ones * threes

    def find_num_combinations(self) -> int:
        combinations = {0: 1}

        def value(index: int):
            return combinations[index] if index in combinations else 0

        for i in self._joltages[1:]:
            combinations[i] = value(i - 1) + value(i - 2) + value(i - 3)

        return combinations[self._joltages[-1]]
