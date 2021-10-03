from advent2020.utils.read_file import ReadFile


class CustomsDeclarations:
    def __init__(self, path: str) -> None:
        self._entries = ReadFile.lines(path)

    def yes_count(self):
        total_count = 0
        group = set()
        for line in self._entries:
            if line == "":
                total_count += len(group)
                group = set()
            else:
                group.update({id for id in line})
        total_count += len(group)
        return total_count
