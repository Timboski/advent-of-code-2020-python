from typing import List


class ReadFile:
    @staticmethod
    def lines(path: str) -> List[str]:
        with open(path) as stream:
            return [entry.strip() for entry in list(stream)]
