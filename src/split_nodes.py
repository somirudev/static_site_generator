import re
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_nodes.append(old_node)
            continue
        parts = re.split(
            rf"({re.escape(delimiter)}[^{re.escape(delimiter)}]+{re.escape(delimiter)})",
            old_node.text,
        )
        for part in parts:
            if part == "":
                continue
            if part.startswith(delimiter) and part.endswith(delimiter):
                text = part[len(delimiter) : -len(delimiter)]
                list_of_nodes.append(TextNode(text, text_type))
            else:
                list_of_nodes.append(TextNode(part, TextType.TEXT))
    return list_of_nodes


def split_nodes_image(old_nodes):
    list_of_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        remaining_text = old_node.text
        if images == []:
            list_of_nodes.append(old_node)
        else:
            for imagetuple in images:
                alt_text, image_url = imagetuple
                text_before, remaining_text = (
                    remaining_text.split(f"![{alt_text}]({image_url})", 1)[0],
                    remaining_text.split(f"![{alt_text}]({image_url})", 1)[1],
                )
                if text_before != "":
                    list_of_nodes.append(TextNode(text_before, TextType.TEXT))
                list_of_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            if remaining_text != "":
                list_of_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return list_of_nodes


def split_nodes_link(old_nodes):
    list_of_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        remaining_text = old_node.text
        if links == []:
            list_of_nodes.append(old_node)
        else:
            for linktuple in links:
                value_text, link_url = linktuple
                text_before, remaining_text = (
                    remaining_text.split(f"[{value_text}]({link_url})", 1)[0],
                    remaining_text.split(f"[{value_text}]({link_url})", 1)[1],
                )
                if text_before != "":
                    list_of_nodes.append(TextNode(text_before, TextType.TEXT))
                list_of_nodes.append(TextNode(value_text, TextType.LINK, link_url))
            if remaining_text != "":
                list_of_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return list_of_nodes
