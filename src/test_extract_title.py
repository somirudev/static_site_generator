import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_title_on_line1(self):
        md = """# this is the title
this is paragraph stuff
blabla
derp"""
        title = extract_title(md)
        self.assertEqual(title, "this is the title")

    def test_title_in_the_middle(self):
        md = """idk why but
the title
# is in the middle of this document
it makes no sense!"""
        title = extract_title(md)
        self.assertEqual(title, "is in the middle of this document")

    def test_no_title(self):
        md = "this text contains no title"
        with self.assertRaises(Exception):
            _ = extract_title(md)


if __name__ == "__main__":
    unittest.main()
