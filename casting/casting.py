import unittest


class TestCasting(unittest.TestCase):

    def test_casting(self):
        a = 1
        b = str(1)
        self.assertEqual(str(type(a)),"<class 'int'>")
        self.assertEqual(str(type(b)),"<class 'str'>")
