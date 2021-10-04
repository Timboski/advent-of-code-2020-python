from typing import Tuple

from advent2020.day8.instruction import Instruction
from advent2020.utils.read_file import ReadFile


class Boot:
    def __init__(self, path: str) -> None:
        self._code = [
            Instruction(idx, line) for idx, line in enumerate(ReadFile.lines(path))
        ]
        self.len = len(self._code)

    def find_acc_at_loop(self) -> int:
        prog_counter, acc = self._run_to_end_or_loop()
        if prog_counter >= self.len:
            raise ValueError("Unexpected boot completion")
        return acc

    def find_acc_after_boot(self) -> int:
        prog_counter, acc = self._run_to_end_or_loop()
        if prog_counter < self.len:
            return None
        if prog_counter != self.len:
            raise ValueError("Prog Counter past end of code")
        return acc
    
    def fix_instruction(self, index: int) -> None:
        self._code[index].fix()

    def _run_to_end_or_loop(self) -> Tuple[int, int]:
        prog_counter = 0
        acc = 0
        while (prog_counter < len(self._code)) and (self._code[prog_counter].never_run):
            prog_counter, acc = self._code[prog_counter].run(acc)
        return prog_counter, acc
