import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_and_quote(self):
        md = """
### This is a level 3 heading with a **bold** word

This is a paragraph

>this is a bunch
>of quotes
>idk why
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a level 3 heading with a <b>bold</b> word</h3><p>This is a paragraph</p><blockquote>this is a bunch\nof quotes\nidk why</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """- one
- two
- three
- four

This is a paragraph"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>one</li><li>two</li><li>three</li><li>four</li></ul><p>This is a paragraph</p></div>",
        )

    def test_ordered_list(self):
        md = """#### heading level 4

1. one
2. two
3. three
4. four"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>heading level 4</h4><ol><li>one</li><li>two</li><li>three</li><li>four</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()
