import unittest


class TestLists(unittest.TestCase):

    def test_list_change_item(self):
        thislist = ["a", "b", "c", "d", "e", "f"]
        thislist[1:1] = ["x", "y"]  # list is inserted at index 1
        print(thislist)

    def test_list_change_item2(self):
        thislist = ["a", "b", "c", "d", "e", "f"]
        thislist[1:4] = ["x", "y"]  # elements with index 1-4 get replaced by x and y
        print(thislist)

    def test_list_change_item3(self):
        thislist = ["apple", "banana", "cherry"]
        print(thislist[-1])
