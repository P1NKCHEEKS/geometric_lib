import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    """Тесты для модуля rectangle"""

    def test_area_zero_width(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_positive_sides(self):
        self.assertEqual(area(3, 4), 12)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_perimeter_string_concatenation(self):
        self.assertEqual(perimeter("3", "4"), "34")

    def test_negative_sides(self):
        self.assertEqual(area(-3, 4), -12)
        self.assertEqual(perimeter(-3, 4), 1)

    def test_empty_string(self):
        self.assertEqual(area("", 4), "")
        with self.assertRaises(TypeError):
            area("", "")
        self.assertEqual(perimeter("", ""), "")

    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            area("3", "4")


if __name__ == '__main__':
    unittest.main()
