from advent2020.day7.bag import Bag
from advent2020.utils.read_file import ReadFile


class Haversacks:
    def __init__(self, path: str) -> None:
        bags = [Bag(line) for line in ReadFile.lines(path)]
        self._bags = {bag.colour: bag for bag in bags}

    def num_colour_options(self) -> int:
        return sum(
            [1 for c in self._bags if self._bags[c].contains("shiny gold", self._bags)])
