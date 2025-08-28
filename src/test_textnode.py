import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noneq_types(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noneq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a different text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_default(self):
        node = TextNode("This is a link node", TextType.LINK, "http://www.google.com/")
        node2 = TextNode("This is a link node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK, "http://www.google.com/")
        node2 = TextNode("This is a link node", TextType.LINK, "http://www.google.com/")
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a link node", TextType.LINK, None)
        node2 = TextNode("This is a link node", TextType.LINK)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
