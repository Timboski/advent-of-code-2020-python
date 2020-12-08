from typing import List

from advent2020.day2.password_entry import PasswordEntry


class PasswordValidation:
    def validate(self, entry: str) -> bool:
        p = PasswordEntry(entry)
        occurances = p.password.count(p.letter)
        return (occurances >= p.min) and (occurances <= p.max)

    def read_report(self, path: str) -> List[int]:
        with open(path) as stream:
            return [entry.strip() for entry in list(stream)]


if __name__ == "__main__":
    pass
