import unittest

class TestSets(unittest.TestCase):

    def test_sets(self):
        set = {1,2,3,2}#items of a set cannot be changed after it is created - good, immutability https://www.w3schools.com/python/python_sets.asp
        print(set)
        print(len(set))
        setOfManyTypes = {1, "a", True}
        print(setOfManyTypes)