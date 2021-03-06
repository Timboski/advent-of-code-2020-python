from advent2020.day2.password_entry import PasswordEntry
from advent2020.day2.password_validation import PasswordValidation


class Puzzle2Validation(PasswordValidation):
    def validate(self, entry: str) -> bool:
        p = PasswordEntry(entry)
        positions = [p.min - 1, p.max - 1]
        matches = sum(1 for index in positions
                      if self.check_index(p.password, index, p.letter))
        return matches == 1

    def check_index(self, password: str, index: int, letter: str):
        if index >= len(password):
            return False
        return password[index] is letter
