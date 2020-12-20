from collections import deque

from advent2020.day4.passport import Passport
from advent2020.utils.read_file import ReadFile


class ProcessPassports:
    def __init__(self,
                 passport_file_path: str,
                 *,
                 validate_contents: bool = True) -> None:
        self._passports = []
        lines = ReadFile.lines(passport_file_path)
        entries = deque(lines)

        while entries:
            self._passports.append(
                Passport(entries, validate_contents=validate_contents))

    @property
    def num_passports(self) -> int:
        return len(self._passports)

    def validate_passports(self) -> int:
        return len([passport for passport in self._passports if passport.validate()])
