import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class ExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_images_but_its_a_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_markdown_images_wrong_syntax(self):
        text = "This text contains wrong syntax for a ![image[(https://i.imgur.com/aKaOqIh.gif)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_markdown_images_wrong_syntax2(self):
        text = "This text contains wrong syntax for a ![image](https://i.im()gur.com/aKaOqIh.gif)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_markdown_images_no_image(self):
        text = "This text contains no images"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_links_but_its_an_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_markdown_links_no_link(self):
        text = "This is text without a link"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [],
            matches,
        )


if __name__ == "__main__":
    unittest.main()
