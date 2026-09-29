from blocktype import *
from htmlnode import *
from textnode import *


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            nodes.append(paragraph_to_htmlnode(block))
        elif block_type == BlockType.HEADING:
            nodes.append(heading_to_htmlnode(block))
        elif block_type == BlockType.QUOTE:
            nodes.append(quote_to_htmlnode(block))
        elif block_type == BlockType.UNORDERED_LIST:
            nodes.append(ulist_to_htmlnode(block))
        elif block_type == BlockType.ORDERED_LIST:
            nodes.append(olist_to_htmlnode(block))
        elif block_type == BlockType.CODE:
            nodes.append(code_to_htmlnode(block))
    return ParentNode("div", nodes)

def paragraph_to_htmlnode(block):
    text = ""
    lines = block.split("\n")
    for line in lines:
        text += line + " "
    children = text_to_children(text.strip())
    return ParentNode("p", children)

def heading_to_htmlnode(block):
        count = 0
        max_index = 7
        if len(block) < 7:
            max_index = len(block)
        for i in range(max_index):
            if block[i] == "#":
                 count += 1
            else:
                 break
        text = block[count + 1:]
        children = text_to_children(text)
        return ParentNode(f"h{count}", children) 
def quote_to_htmlnode(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[1:]
        children = text_to_children(text.strip())
        items.extend(children)
    return ParentNode("blockquote", items)

def ulist_to_htmlnode(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def olist_to_htmlnode(block):
    lines = block.split("\n")
    items = []
    for line in lines:
        count = 0
        for c in line:
            if (c != " "):
                count += 1
            else:
                count += 1
                break

        text = line[count:]
        children = text_to_children(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def code_to_htmlnode(block):
    text = block[4:-3]
    node = TextNode(text.strip(), TextType.CODE)
    children = [text_node_to_html_node(node),]
    return ParentNode("pre", children)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        lines = block.split('\n')
        for line in lines:
            if line[0:2] == "# ":
                return line[2:]
    raise Exception("Error: No h1 header found")
