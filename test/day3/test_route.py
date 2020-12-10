import unittest

from advent2020.day3.route import Route


class TestRoute(unittest.TestCase):
    def test_example_puzzle1(self):
        # Arrange
        example_input = "test/day3/example_input"
        sut = Route(example_input)

        # Act
        trees_encountered = sut.toboggan_run(3, 1)

        # Assert
        self.assertEqual(trees_encountered, 7)

    def test_validate_puzzle1_answer(self):
        # Arrange
        example_input = "advent2020/day3/input"
        sut = Route(example_input)

        # Act
        trees_encountered = sut.toboggan_run(3, 1)

        # Assert
        self.assertEqual(trees_encountered, 171)

    def test_example_puzzle2_routes(self):
        # Arrange
        example_input = "test/day3/example_input"
        sut = Route(example_input)

        # Act
        trees_encountered = [sut.toboggan_run(1, 1)]  # Right 1, down 1.
        trees_encountered.append(sut.toboggan_run(3, 1))  # Right 3, down 1.
        trees_encountered.append(sut.toboggan_run(5, 1))  # Right 5, down 1.
        trees_encountered.append(sut.toboggan_run(7, 1))  # Right 7, down 1.
        trees_encountered.append(sut.toboggan_run(1, 2))  # Right 1, down 2.

        # Assert
        self.assertSequenceEqual(trees_encountered, [2, 7, 3, 4, 2])

    def test_example_puzzle2_total(self):
        # Arrange
        example_input = "test/day3/example_input"
        sut = Route(example_input)

        # Act
        trees_encountered = sut.toboggan_run(1, 1)  # Right 1, down 1.
        trees_encountered *= sut.toboggan_run(3, 1)  # Right 3, down 1.
        trees_encountered *= sut.toboggan_run(5, 1)  # Right 5, down 1.
        trees_encountered *= sut.toboggan_run(7, 1)  # Right 7, down 1.
        trees_encountered *= sut.toboggan_run(1, 2)  # Right 1, down 2.

        # Assert
        self.assertEqual(trees_encountered, 336)
