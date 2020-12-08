class PasswordEntry:
    def __init__(self, entry: str) -> None:
        '''Split string entry into constituent parts'''
        '''f"{min}-{max} {letter}: {password}'''
        (min, remainder) = entry.split("-", 1)
        self.min = int(min)

        (max, remainder) = remainder.split(" ", 1)
        self.max = int(max)

        (self.letter, self.password) = remainder.split(": ", 1)
