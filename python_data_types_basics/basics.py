import unittest

class TestBasics(unittest.TestCase):

    def test_multiple_variables(self):
        x = y = z = "same string"
        self.assertEqual(x, "same string")
        self.assertEqual(y, "same string")
        self.assertEqual(z, "same string")

        fruits = ["apple", "banana", "cherry"]
        x, y, z = fruits
        self.assertEqual(x, "apple")
        self.assertEqual(y, "banana")
        self.assertEqual(z, "cherry")

        x, y, z = "x", "y", "z"
        self.assertEqual(x, "x")
        self.assertEqual(y, "y")
        self.assertEqual(z, "z")
