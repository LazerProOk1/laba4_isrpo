import unittest

import circle
import rectangle
import square
import triangle


class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(2), 12.566370614359172)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.566370614359172)

    def test_zero(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)

    def test_float(self):
        self.assertAlmostEqual(circle.area(0.5), 0.7853981633974483)
        self.assertAlmostEqual(circle.perimeter(0.5), 3.141592653589793)


class RectangleTest(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_zero(self):
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area(3, 0), 0)
        self.assertEqual(rectangle.area(0, 0), 0)

        self.assertEqual(rectangle.perimeter(0, 5), 10)
        self.assertEqual(rectangle.perimeter(3, 0), 6)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_float(self):
        self.assertAlmostEqual(rectangle.area(2.5, 1.5), 3.75)
        self.assertAlmostEqual(rectangle.perimeter(2.5, 1.5), 8)

    def test_square(self):
        self.assertEqual(rectangle.area(4, 4), 16)
        self.assertEqual(rectangle.perimeter(4, 4), 16)


class SquareTest(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(4), 16)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_zero(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.perimeter(0), 0)

    def test_float(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)
        self.assertAlmostEqual(square.perimeter(1.5), 6)


class TriangleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(triangle.area(3, 4, 5), 6)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_equal_sides(self):
        self.assertAlmostEqual(triangle.area(2, 2, 2), 1.7320508075688772)
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_two_equal_sides(self):
        self.assertAlmostEqual(triangle.area(5, 5, 6), 12)
        self.assertEqual(triangle.perimeter(5, 5, 6), 16)

    def test_zero(self):
        self.assertEqual(triangle.area(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_float(self):
        self.assertAlmostEqual(triangle.area(1.5, 2, 2.5), 1.5)
        self.assertAlmostEqual(triangle.perimeter(1.5, 2, 2.5), 6)

    def test_line(self):
        self.assertEqual(triangle.area(1, 2, 3), 0)
        self.assertEqual(triangle.perimeter(1, 2, 3), 6)


if __name__ == "__main__":
    unittest.main()