from collections import deque
from typing import List

from advent2020.day4.passport import Passport


class ProcessPassports:
    def __init__(self, passport_file_path: str) -> None:
        self._passports = []
        lines = self._read_file(passport_file_path)
        entries = deque(lines)

        while entries:
            self._passports.append(Passport(entries))

    @property
    def num_passports(self) -> int:
        return len(self._passports)

    def validate_passports(self) -> int:
        return len([passport for passport in self._passports if passport.validate()])

    @staticmethod
    def _read_file(path: str) -> List[str]:
        with open(path) as stream:
            return [entry.strip() for entry in list(stream)]
