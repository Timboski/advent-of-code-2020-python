from advent2020.day2.password_entry import PasswordEntry
from advent2020.day2.password_validation import PasswordValidation


class Puzzle1Validation(PasswordValidation):
    def validate(self, entry: str) -> bool:
        p = PasswordEntry(entry)
        occurances = p.password.count(p.letter)
        return (occurances >= p.min) and (occurances <= p.max)


if __name__ == "__main__":
    path = "/workspaces/advent-of-code-2020-python/advent2020/day2/input"
    validator = Puzzle1Validation()
    print(validator.count_valid_entries_in_file(path))
