import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_default(self):
        node = HTMLNode()
        teststring = "HTMLNode(None, None, None, )"
        self.assertEqual(teststring, repr(node))

    def test_tag(self):
        node = HTMLNode("test_tag")
        teststring = "HTMLNode(test_tag, None, None, )"
        self.assertEqual(teststring, repr(node))

    def test_value(self):
        node = HTMLNode("test_tag", "test_value")
        teststring = "HTMLNode(test_tag, test_value, None, )"
        self.assertEqual(teststring, repr(node))

    def test_children(self):
        child = HTMLNode()
        childstring = "HTMLNode(None, None, None, )"
        node = HTMLNode("test_tag", None, [child])
        teststring = f"HTMLNode(test_tag, None, [{childstring}], )"
        self.assertEqual(teststring, repr(node))

    def test_props(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        teststring = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(teststring, node.props_to_html())

    def test_props_in_node(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        teststring = (
            'HTMLNode(None, None, None,  href="https://www.google.com" target="_blank")'
        )
        self.assertEqual(teststring, repr(node))


if __name__ == "__main__":
    unittest.main()
