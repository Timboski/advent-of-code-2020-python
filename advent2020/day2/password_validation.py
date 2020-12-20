from advent2020.utils.read_file import ReadFile


class PasswordValidation:
    def validate(self, entry: str) -> bool:
        return True

    def count_valid_entries_in_file(self, path: str) -> int:
        entries = ReadFile.lines(path)
        return sum(1 for entry in entries if self.validate(entry))
