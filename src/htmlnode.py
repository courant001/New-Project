class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ""
        if self.props == None:
            return ""
        elif self.props == "":
            return ""
        else:
            for k, v in self.props.items():
                html_string += f' {k}="{v}"'
        return html_string
    def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
            if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
                return True

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
       return f"LeafNode({self.tag}, {self.value}, {self.props})"

    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
            super().__init__(tag, value=None, children=children, props=props)
    def to_html(self):
        html_children = ""
        if self.tag is None:
            raise ValueError("tag required")
        if self.children is None:
            raise ValueError("children required")
        
        else:
            for n in self.children:
                html_children += n.to_html()

            return f"<{self.tag}{self.props_to_html()}>{html_children}</{self.tag}>"
        
