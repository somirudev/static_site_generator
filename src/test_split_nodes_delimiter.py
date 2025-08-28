from re import split
import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TextSplitNodesDelimiter(unittest.TestCase):
    def test_simplecode(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_bold(self):
        node = TextNode("This text **contains** a few **bold** words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This text ", TextType.TEXT),
                TextNode("contains", TextType.BOLD),
                TextNode(" a few ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" words", TextType.TEXT),
            ],
        )

    def test_start_with_delimiter(self):
        node = TextNode("`code block` at the start", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("code block", TextType.CODE),
                TextNode(" at the start", TextType.TEXT),
            ],
        )

    def test_end_with_delimiter(self):
        node = TextNode("This text ends with a bold **word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This text ends with a bold ", TextType.TEXT),
                TextNode("word", TextType.BOLD),
            ],
        )

    def test_exception(self):
        node = TextNode("This ` gives an error", TextType.TEXT)
        with self.assertRaises(Exception):
            _ = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_not_a_text_node(self):
        node = TextNode("This bold text contains _italic_ words", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertNotEqual(
            new_nodes,
            [
                TextNode("This bold text contains ", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode(" words", TextType.BOLD),
            ],
        )

    def test_not_a_text_node2(self):
        node = TextNode("This bold text contains _italic_ words", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [TextNode("This bold text contains _italic_ words", TextType.BOLD)],
        )

    def test_double_nodes(self):
        node = TextNode("**bold words** at the start", TextType.TEXT)
        node2 = TextNode("This text has a **bold** word in the middle", TextType.TEXT)
        node3 = TextNode("This text ends with a bold **word**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2, node3], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("bold words", TextType.BOLD),
                TextNode(" at the start", TextType.TEXT),
                TextNode("This text has a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word in the middle", TextType.TEXT),
                TextNode("This text ends with a bold ", TextType.TEXT),
                TextNode("word", TextType.BOLD),
            ],
        )

    def test_double_delimiters(self):
        node = TextNode("This text has **weird****bold****syntax**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This text has ", TextType.TEXT),
                TextNode("weird", TextType.BOLD),
                TextNode("bold", TextType.BOLD),
                TextNode("syntax", TextType.BOLD),
            ],
        )


if __name__ == "__main__":
    unittest.main()
