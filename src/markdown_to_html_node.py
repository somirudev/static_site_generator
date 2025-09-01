import re
from markdown_to_blocks import markdown_to_blocks
from blocktypes import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.paragraph:
                # create list of grandchildren and nest inside paragraph tag
                block = block.replace("\n", " ")
                grandchildren = text_to_children(block)
                children.append(ParentNode("p", grandchildren))
            case BlockType.heading:
                heading = re.match(r"^(#{1,6})\s(.*)", block)
                # split heading into level and text
                heading_level = len(heading.group(1))
                heading_text = heading.group(2)
                grandchildren = text_to_children(heading_text)
                children.append(ParentNode(f"h{heading_level}", grandchildren))
            case BlockType.code:
                # create code node and nest it within a pre tag
                lines = block.split("\n")
                code_block = "\n".join(lines[1:-1]) + "\n"
                children.append(
                    ParentNode(
                        "pre", [ParentNode("code", [LeafNode(None, code_block)])]
                    )
                )
            case BlockType.ordered_list:
                lines = block.split("\n")
                list_nodes = []
                for line in lines:
                    # remove "X. " where X is the ordered list number and convert to list nodes
                    line_nodes = text_to_children(line[3:])
                    list_nodes.append(ParentNode("li", line_nodes))
                # nest list nodes within ordered list tag
                children.append(ParentNode("ol", list_nodes))
            case BlockType.unordered_list:
                lines = block.split("\n")
                list_nodes = []
                for line in lines:
                    # remove "- " and convert to list node
                    line_nodes = text_to_children(line[2:])
                    list_nodes.append(ParentNode("li", line_nodes))
                # next list nodes within unordered list tag
                children.append(ParentNode("ul", list_nodes))
            case BlockType.quote:
                lines = block.split("\n")
                quote_lines = []
                for line in lines:
                    # remove ">"
                    quote_lines.append(line[1:])
                quote_nodes = text_to_children("\n".join(quote_lines))
                # list quote nodes within blockquote tag
                children.append(ParentNode("blockquote", quote_nodes))
            case _:
                raise Exception("node does not have a valid block type")
    return ParentNode("div", children)


def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for node in textnodes:
        htmlnodes.append(text_node_to_html_node(node))
    return htmlnodes
