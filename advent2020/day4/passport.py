from collections import deque


class Passport:
    REQUIRED_FIELDS = [
        "byr",  # Birth Year
        "iyr",  # Issue Year
        "eyr",  # Expiration Year
        "hgt",  # Height
        "hcl",  # Hair Color
        "ecl",  # Eye Color
        "pid",  # Passport ID
        # "cid"   # Country ID
    ]

    def __init__(self, passport_entries: deque) -> None:
        self._fields = {}
        while passport_entries:
            entry = passport_entries.pop()
            if not entry:
                return
            self._add_entry(entry)

    def validate(self) -> bool:
        for required_field in self.REQUIRED_FIELDS:
            if required_field not in self._fields:
                return False
        return True

    def _add_entry(self, entry: str):
        fields = entry.split(" ")
        for field in fields:
            (key, value) = field.split(":")
            self._fields[key] = value
