import functools
import math
import unittest


def lcm(*args):
    return functools.reduce(lambda a, b: a * b // math.gcd(a, b), args)


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(lcm(2, 5), 10)

    def test_2(self):
        self.assertEqual(lcm(2, 3, 4), 12)

    def test_3(self):
        self.assertEqual(lcm(9), 9)

    def test_4(self):
        self.assertEqual(lcm(0), 0)

    def test_5(self):
        self.assertEqual(lcm(0, 1), 0)

    def test_6(self):
        self.assertEqual(lcm(2, 3, 4, 10, 20), 60)

    def test_7(self):
        self.assertEqual(lcm(5, 2, 8, 24, 60), 120)


if __name__ == "__main__":
    unittest.main()