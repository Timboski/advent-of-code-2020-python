from collections import deque


class Passport:
    def __init__(self, passport_entries: deque, *, validate_contents: bool) -> None:
        self._field_validation_map = self._create_field_validation_map()
        self._validate_contents = validate_contents
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
            if self._validate_contents:
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

    @staticmethod
    def _create_field_validation_map() -> dict:
        return {
            "byr": Passport._validate_birth_year,
            "iyr": Passport._validate_issue_year,
            "eyr": Passport._validate_expiration_year,
            "hgt": Passport._validate_height,
            "hcl": Passport._validate_hair_color,
            "ecl": Passport._validate_eye_color,
            "pid": Passport._validate_passport_id,
            # "cid"   # Country ID
        }

    @staticmethod
    def _validate_birth_year(entry: str) -> bool:
        '''byr (Birth Year) - four digits; at least 1920 and at most 2002.'''
        return Passport._validate_digits(entry, min=1920, max=2002)

    @staticmethod
    def _validate_issue_year(entry: str) -> bool:
        '''iyr (Issue Year) - four digits; at least 2010 and at most 2020.'''
        return Passport._validate_digits(entry, min=2010, max=2020)

    @staticmethod
    def _validate_expiration_year(entry: str) -> bool:
        '''eyr (Expiration Year) - four digits; at least 2020 and at most 2030.'''
        return Passport._validate_digits(entry, min=2020, max=2030)

    @staticmethod
    def _validate_height(entry: str) -> bool:
        '''
        hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
        '''
        if "cm" in entry:
            height = entry.removesuffix("cm")
            return Passport._validate_digits(height, min=150, max=193)
        if "in" in entry:
            height = entry.removesuffix("in")
            return Passport._validate_digits(height, min=59, max=76)
        return False

    @staticmethod
    def _validate_hair_color(entry: str) -> bool:
        '''hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.'''
        if len(entry) != 7:
            return False
        colour = entry.removeprefix("#")
        if len(colour) != 6:
            return False
        for char in colour:
            if char not in "0123456789abcdef":
                return False
        return True

    @staticmethod
    def _validate_eye_color(entry: str) -> bool:
        '''ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.'''
        valid_eye_colours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        return entry in valid_eye_colours

    @staticmethod
    def _validate_passport_id(entry: str) -> bool:
        '''pid (Passport ID) - a nine-digit number, including leading zeroes.'''
        if len(entry) != 9:
            return False
        return Passport._validate_digits(entry, min=0, max=999999999)

    @staticmethod
    def _validate_digits(entry: str, *, min: int, max: int) -> bool:
        if not entry.isdigit():
            return False
        year = int(entry)
        return year >= min and year <= max
