from advent2020.day8.boot import Boot


class BootFixer:
    def __init__(self, path: str) -> None:
        self._path = path

    def fix_and_run(self) -> int:
        fix_index = 0
        while True:
            boot = Boot(self._path)
            boot.fix_instruction(fix_index)
            acc = boot.find_acc_after_boot()
            if acc is not None:
                return acc
            fix_index += 1
