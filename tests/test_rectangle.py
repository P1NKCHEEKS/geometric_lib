import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    """Тесты для модуля rectangle (прямоугольник)."""

    def test_area_zero_width(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_positive_sides(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4), 14)


if __name__ == '__main__':
    unittest.main()
