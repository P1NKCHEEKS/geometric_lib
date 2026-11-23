import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """Тесты для модуля circle (круг)."""

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)


if __name__ == '__main__':
    unittest.main()
