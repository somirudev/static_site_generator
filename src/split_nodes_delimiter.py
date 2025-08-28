from textnode import TextNode, TextType


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
