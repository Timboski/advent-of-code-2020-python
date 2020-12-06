import unittest
from typing import List


class ReportRepair(unittest.TestCase):
    def parse(self, entries: List[int]) -> int:
        for entry1 in entries:
            for entry2 in entries:
                if entry1 + entry2 == 2020:
                    return entry1 * entry2
