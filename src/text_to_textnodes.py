from split_nodes import split_nodes_link, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType


def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    image_split_nodes = split_nodes_image([initial_node])
    link_split_nodes = split_nodes_link(image_split_nodes)
    bold_split_nodes = split_nodes_delimiter(link_split_nodes, "**", TextType.BOLD)
    italic_split_nodes = split_nodes_delimiter(bold_split_nodes, "_", TextType.ITALIC)
    code_split_nodes = split_nodes_delimiter(italic_split_nodes, "`", TextType.CODE)
    return code_split_nodes
