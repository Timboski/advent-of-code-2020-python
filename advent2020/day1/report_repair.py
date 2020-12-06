import unittest
from typing import List


class ReportRepair(unittest.TestCase):
    def parse(self, entries: List[int]) -> int:
        for entry1 in entries:
            for entry2 in entries:
                if entry1 + entry2 == 2020:
                    return entry1 * entry2

    def read_report(self, path: str) -> List[int]:
        return [int(entry) for entry in list(open(path))]


if __name__ == "__main__":
    repair = ReportRepair()
    input_data = repair.read_report("/workspaces/advent-of-code-2020-python/advent2020/day1/input")
    result = repair.parse(input_data)
    print(result)
