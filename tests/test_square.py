import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    """Тесты для модуля square"""

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_side(self):
        self.assertEqual(area(5), 25)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_string_concatenation(self):
        self.assertEqual(perimeter("5"), "5555")


if __name__ == '__main__':
    unittest.main()
