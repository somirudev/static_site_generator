import unittest
from blocktypes import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading1(self):
        block = "# testing"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.heading)

    def test_heading6(self):
        block = "###### testing"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.heading)

    def test_heading_invalid(self):
        block = "####### testing"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_code(self):
        block = """```code block
with multiple lines```"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.code)

    def test_code_invalid(self):
        block = """```code block
with multiple lines```
but invalid"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_quote(self):
        block = """> this quote block
> consisted of multiple
> lines"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.quote)

    def test_quote_invalid(self):
        block = """> this quote block
is missing a >
> in line two"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_unordered_list(self):
        block = """- one
- two
- three"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.unordered_list)

    def test_unordered_list_invalid(self):
        block = """- one
- two
three"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.paragraph)

    def test_ordered_list(self):
        block = """1. one
2. two
3. three"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.ordered_list)

    def test_ordered_list_invalid(self):
        block = """1. one
3. two
4. three"""
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.paragraph)


if __name__ == "__main__":
    unittest.main()
