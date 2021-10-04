import unittest

from advent2020.day8.instruction import Instruction
from parameterized import parameterized


class TestInstruction(unittest.TestCase):
    @parameterized.expand([
        ("nop +0", "nop", 0),
        ("neg -0", "neg", 0),
        ("acc -99", "acc", -99),
        ("tst 1337", "tst", 1337),
    ])
    def test_example_input(self, line: str, op: str, value: int):
        # Arrange, Act
        sut = Instruction(0, line)

        # Assert
        self.assertEqual(sut.op, op)
        self.assertEqual(sut.value, value)
