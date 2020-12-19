from collections import deque


class Passport:
    def __init__(self, passport_entries: deque) -> None:
        passport_entries.pop()
