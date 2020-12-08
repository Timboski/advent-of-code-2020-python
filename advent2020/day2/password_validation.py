from typing import List


class PasswordValidation:
    def validate(self, entry: str) -> bool:
        return True

    def read_entries_from_file(self, path: str) -> List[int]:
        with open(path) as stream:
            return [entry.strip() for entry in list(stream)]

    def count_valid_entries_in_file(self, path: str) -> int:
        entries = self.read_entries_from_file(path)
        return sum(1 for entry in entries if self.validate(entry))
