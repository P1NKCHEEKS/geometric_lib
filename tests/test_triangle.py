import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    """Тесты для модуля triangle """

    def test_area_zero_height(self):
        self.assertEqual(area(5, 0), 0)

    def test_area_positive_values(self):
        self.assertEqual(area(6, 4), 12.0)

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_string_concatenation(self):
        self.assertEqual(perimeter("3", "4", "5"), "345")

    def test_negative_values(self):
        self.assertEqual(area(-6, 4), -12.0)
        self.assertEqual(perimeter(-3, 4, 5), 6)

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            area("", 4)
        self.assertEqual(perimeter("", "", ""), "")

    def test_area_string_raises(self):
        with self.assertRaises(TypeError):
            area("6", "4")


if __name__ == '__main__':
    unittest.main()
