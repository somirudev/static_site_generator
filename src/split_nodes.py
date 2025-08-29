from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            list_of_nodes.append(old_node)
        else:
            list_of_parts = old_node.text.split(delimiter)
            if len(list_of_parts) % 2 == 0 and not (
                old_node.text[-1] == delimiter or old_node.text[0] == delimiter
            ):
                raise Exception("no closing delimiter, invalid Markdown syntax")
            for i in range(len(list_of_parts)):
                if list_of_parts[i] == "":
                    continue
                if i % 2 == 0:
                    list_of_nodes.append(TextNode(list_of_parts[i], TextType.TEXT))
                else:
                    list_of_nodes.append(TextNode(list_of_parts[i], text_type))
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
