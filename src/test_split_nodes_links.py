import unittest
from split_nodes import split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://www.google.com) and another [link2](https://www.yahoo.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://www.yahoo.com"),
            ],
        )

    def test_initial_link(self):
        node = TextNode("[link](https://www.github.com) that was a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("link", TextType.LINK, "https://www.github.com"),
                TextNode(" that was a link", TextType.TEXT),
            ],
        )

    def test_ending_with_image(self):
        node = TextNode(
            "This is _a link_: [link](https://www.netflix.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is _a link_: ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.netflix.com"),
            ],
        )

    def test_no_links(self):
        node = TextNode(
            "This text has no links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(new_nodes, [node])

    def test_multiple_nodes_at_once(self):
        node1 = TextNode(
            "This is text with an [link](https://www.google.com) and another [link2](https://www.yahoo.com)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "[link](https://www.github.com) that was a link", TextType.TEXT
        )
        node3 = TextNode(
            "This is _a link_: [link](https://www.netflix.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node1, node2, node3])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://www.yahoo.com"),
                TextNode("link", TextType.LINK, "https://www.github.com"),
                TextNode(" that was a link", TextType.TEXT),
                TextNode("This is _a link_: ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.netflix.com"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
