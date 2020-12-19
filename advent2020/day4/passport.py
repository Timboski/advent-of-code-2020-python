from collections import deque


class Passport:
    def __init__(self, passport_entries: deque) -> None:
        while passport_entries:
            entry = passport_entries.pop()
            if not entry:
                return
