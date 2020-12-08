from advent2020.day2.password_entry import PasswordEntry


class PasswordValidation:
    def validate(self, entry: str) -> bool:
        p = PasswordEntry(entry)
        occurances = p.password.count(p.letter)
        return (occurances >= p.min) and (occurances <= p.max)
