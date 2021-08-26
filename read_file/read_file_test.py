import unittest


class TestReadingFile(unittest.TestCase):

    def test_read_file_content(self):
        file_content = open("demofile.txt", "r").read()
        self.assertEqual(file_content, "testing hey python")
