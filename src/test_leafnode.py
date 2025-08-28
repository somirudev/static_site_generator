import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_code(self):
        node = LeafNode("code", 'print("Hello, world!")')
        self.assertEqual(node.to_html(), '<code>print("Hello, world!")</code>')

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        teststring = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), teststring)

    def test_value_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_empty_tag(self):
        string = "This is just plain text"
        node = LeafNode(None, string)
        self.assertEqual(node.to_html(), string)


if __name__ == "__main__":
    unittest.main()
