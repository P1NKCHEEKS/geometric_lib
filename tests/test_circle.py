import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """Тесты для модуля circle """

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(2), 12.566370614359172)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(2), 12.566370614359172)


if __name__ == '__main__':
    unittest.main()
