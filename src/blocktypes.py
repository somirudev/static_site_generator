from enum import Enum
import re

BlockType = Enum(
    "BlockType",
    ["paragraph", "heading", "code", "quote", "unordered_list", "ordered_list"],
)


def block_to_block_type(block):
    if re.search(r"^#{1,6}\s.+$", block) is not None:
        return BlockType.heading
    if re.search(r"^```.*?```$", block, re.DOTALL) is not None:
        return BlockType.code
    lines = block.split("\n")
    if all(re.match(r"^>", line) for line in lines):
        return BlockType.quote
    if all(re.match(r"^[-*+]\s", line) for line in lines):
        return BlockType.unordered_list

    isorderedlist = True
    for i, line in enumerate(lines, 1):
        if not re.match(rf"^{i}\.\s", line):
            isorderedlist = False
            break
    if isorderedlist:
        return BlockType.ordered_list
    return BlockType.paragraph
