import unittest
from typing import List


class ReportRepair(unittest.TestCase):
    def find_2_numbers(self, entries: List[int]) -> int:
        for entry1 in entries:
            for entry2 in entries:
                if entry1 + entry2 == 2020:
                    print(f"{entry1} + {entry2} = 2020")
                    print(f"{entry1} * {entry2} = {entry1 * entry2}")
                    return entry1 * entry2

    def find_3_numbers(self, entries: List[int]) -> int:
        for entry1 in entries:
            for entry2 in entries:
                for entry3 in entries:
                    if entry1 + entry2 + entry3 == 2020:
                        answer = entry1 * entry2 * entry3
                        print(f"{entry1} + {entry2} + {entry3} = 2020")
                        print(f"{entry1} * {entry2} * {entry3}  = {answer}")
                        return answer

    def read_report(self, path: str) -> List[int]:
        return [int(entry) for entry in list(open(path))]


if __name__ == "__main__":
    repair = ReportRepair()
    input_data = repair.read_report(
        "/workspaces/advent-of-code-2020-python/advent2020/day1/input")
    result = repair.find_2_numbers(input_data)
    print(result)
