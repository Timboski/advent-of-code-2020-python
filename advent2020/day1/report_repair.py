import math
import unittest
from typing import Set, Tuple


class ReportRepair(unittest.TestCase):
    def find_2_numbers(self, entries: Set[int]) -> int:
        (num1, num2) = self._find_two_numbers(entries, 2020)
        return self._print_and_return_answer(num1, num2)

    def find_3_numbers(self, entries: Set[int]) -> int:
        for entry in entries:
            remainder = 2020 - entry
            result = self._find_two_numbers(entries, remainder)
            if result:
                (num1, num2) = result
                return self._print_and_return_answer(entry, num1, num2)

    def read_report(self, path: str) -> Set[int]:
        return {int(entry) for entry in list(open(path))}

    def _find_two_numbers(self, entries: Set[int], target: int) -> Tuple[int]:
        for entry in entries:
            remainder = target - entry
            if remainder in entries:
                return (entry, remainder)

    def _print_and_return_answer(self, *numbers: int):
        answer = math.prod(numbers)
        num_str = [str(num) for num in numbers]
        print(f"{' + '.join(num_str)} = 2020")
        print(f"{' * '.join(num_str)}  = {answer}")
        return answer


if __name__ == "__main__":
    repair = ReportRepair()
    input_data = repair.read_report(
        "/workspaces/advent-of-code-2020-python/advent2020/day1/input")

    repair.find_2_numbers(input_data)

    repair.find_3_numbers(input_data)
