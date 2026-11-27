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

    def test_negative_radius(self):
        self.assertAlmostEqual(area(-2), 12.566370614359172)
        self.assertAlmostEqual(perimeter(-2), -12.566370614359172)

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            area("")
        with self.assertRaises(TypeError):
            perimeter("")

    def test_string_argument(self):
        with self.assertRaises(TypeError):
            area("2")
        with self.assertRaises(TypeError):
            perimeter("2")


if __name__ == '__main__':
    unittest.main()
