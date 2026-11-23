import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    """Тесты для модуля triangle (треугольник)."""

    def test_area_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_area_positive_values(self):
        self.assertEqual(area(6, 4), 12.0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)


if __name__ == '__main__':
    unittest.main()
