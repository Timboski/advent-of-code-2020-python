from typing import Tuple
from unittest import case


class Instruction:
    def __init__(self, index: int, line: str) -> None:
        self.index = index
        self.op, value = line.split(" ")
        self.value = int(value)
        self.never_run = True

    def run(self, acc: int) -> Tuple[int, int]:
        self.never_run = False
        if self.op == "nop":
            return self.index + 1, acc
        if self.op == "acc":
            return self.index + 1, acc + self.value
        if self.op == "jmp":
            return self.index + self.value, acc
        raise ValueError(f"Unexpected op code: {self.op}")
