from collections import deque


class Passport:
    def __init__(self, passport_entries: deque) -> None:
        self._field_validation_map = self._create_field_validation_map()
        self._fields = {}
        while passport_entries:
            entry = passport_entries.pop()
            if not entry:
                return
            self._add_entry(entry)

    def validate(self) -> bool:
        for required_field in self._field_validation_map:
            if required_field not in self._fields:
                return False
            validation = self._field_validation_map[required_field]
            field_value = self._fields[required_field]
            if not validation(field_value):
                return False
        return True

    def _add_entry(self, entry: str):
        fields = entry.split(" ")
        for field in fields:
            (key, value) = field.split(":")
            self._fields[key] = value

    def _create_field_validation_map(self) -> dict:
        return {
            "byr": self._validate_birth_year,
            "iyr": self._validate_issue_year,
            "eyr": self._validate_expiration_year,
            "hgt": self._validate_height,
            "hcl": self._validate_hair_color,
            "ecl": self._validate_eye_color,
            "pid": self._validate_passport_id,
            # "cid"   # Country ID
        }

    def _validate_birth_year(sel, entry: str) -> bool:
        return True

    def _validate_issue_year(self, entry: str) -> bool:
        return True

    def _validate_expiration_year(self, entry: str) -> bool:
        return True

    def _validate_height(self, entry: str) -> bool:
        return True

    def _validate_hair_color(self, entry: str) -> bool:
        return True

    def _validate_eye_color(self, entry: str) -> bool:
        return True

    def _validate_passport_id(self, entry: str) -> bool:
        return True
