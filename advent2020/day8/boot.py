from advent2020.day8.instruction import Instruction
from advent2020.utils.read_file import ReadFile


class Boot:
    def __init__(self, path: str) -> None:
        self._code = [
            Instruction(idx, line) for idx, line in enumerate(ReadFile.lines(path))
        ]

    def find_acc_at_loop(self) -> int:
        prog_counter = 0
        acc = 0
        while self._code[prog_counter].never_run:
            prog_counter, acc = self._code[prog_counter].run(acc)
        return acc
