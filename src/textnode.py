from enum import Enum
from htmlnode import *
from inline_markdown import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
       return LeafNode("a", text_node.text, {"href": text_node.url})         
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img","", {"src": text_node.url, "alt" : text_node.text})  
        
    else:
        raise Exception(f"Invalid parameters")

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    result = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        node_str = old_node.text
        split_text = node_str.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i, part in enumerate(split_text):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(split_text[i], TextType.TEXT))
            else:
                result.append(TextNode(split_text[i], text_type))
            
        
    return result

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                    result.append(old_node)
                    continue
            original_text = old_node.text
            extracted = extract_markdown_images(original_text)
            if len(extracted) == 0:
                result.append(old_node)
                continue
            for item in extracted:
                sections = original_text.split(f"![{item[0]}]({item[1]})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown, image section not closed")
                if sections[0] != "":
                    result.append(TextNode(sections[0], TextType.TEXT))
                result.append(TextNode(item[0], TextType.IMAGE, item[1],))
                original_text = sections[1]

            if original_text != "":
                result.append(TextNode(original_text, TextType.TEXT))
            
    return result

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        original_text = old_node.text
        extracted = extract_markdown_links(original_text)
        if len(extracted) == 0:
            result.append(old_node)
            continue
        for link in extracted:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.TEXT))
    return result

def text_to_textnodes(text):
    first_node = TextNode(text, TextType.TEXT)
    nodes = [first_node,]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
def markdown_to_blocks(markdown):
    result = []
    split_str = markdown.split("\n\n")
    for s in split_str:
        s = s.strip()
        if len(s) == 0:
            continue
        else:
            result.append(s)
    return result