from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("all parent nodes must have children")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
