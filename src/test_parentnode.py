import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("li", "child")
        child_node2 = LeafNode("li", "child2")
        parent_node = ParentNode("ul", [child_node, child_node2])
        self.assertEqual(
            parent_node.to_html(), "<ul><li>child</li><li>child2</li></ul>"
        )

    def test_to_html_with_subtree(self):
        title_node = LeafNode("h1", "This is the title")
        list_node = LeafNode("li", "child")
        list_node2 = LeafNode("li", "child2")
        parent_node = ParentNode("ol", [list_node, list_node2])
        grandparent_node = ParentNode("body", [title_node, parent_node])
        self.assertEqual(
            grandparent_node.to_html(),
            "<body><h1>This is the title</h1><ol><li>child</li><li>child2</li></ol></body>",
        )

    def test_tag_error(self):
        child_node = LeafNode("p", "child")
        node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_error(self):
        node = ParentNode("ol", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_children_empty_list(self):
        node = ParentNode("ol", [])
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
