from typing import List

from advent2020.day2.password_entry import PasswordEntry


class PasswordValidation:
    def validate(self, entry: str) -> bool:
        p = PasswordEntry(entry)
        occurances = p.password.count(p.letter)
        return (occurances >= p.min) and (occurances <= p.max)

    def read_entries_from_file(self, path: str) -> List[int]:
        with open(path) as stream:
            return [entry.strip() for entry in list(stream)]

    def count_valid_entries_in_file(self, path: str) -> int:
        entries = self.read_entries_from_file(path)
        return sum(1 for entry in entries if self.validate(entry))


if __name__ == "__main__":
    pass
