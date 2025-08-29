import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNode(unittest.TestCase):
    def test_everything_once(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode(
                    "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
        )

    def test_no_images_or_links(self):
        text = "This is **text** with multiple **bold** text parts and also _some_ `code block` and _italics_"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with multiple ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text parts and also ", TextType.TEXT),
                TextNode("some", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("italics", TextType.ITALIC),
            ],
        )

    def test_multiple_images(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png) that **was** an image. This is _text with another_ ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png). The images never stop! ![image](https://i.imgur.com/zjjcJKZ.png)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" that ", TextType.TEXT),
                TextNode("was", TextType.BOLD),
                TextNode(" an image. This is ", TextType.TEXT),
                TextNode("text with another", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(". The images never stop! ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
        )

    if __name__ == "__main__":
        unittest.main()
