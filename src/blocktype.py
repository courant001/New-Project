from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block):
    lines = block.split('\n')
    if block[0] == "#":
        return BlockType.HEADING
    elif block[0:3] == "```":
        return BlockType.CODE
    check = True
    for i in range(len(lines)):
        if lines[i][0] !=  ">":
            check = False
    
    if check is True:
        return BlockType.QUOTE
    check = True
    for i in range(len(lines)):
        if lines[i][0] !=  "-":
            check = False
    if check is True:
        return BlockType.UNORDERED_LIST
    check = True
    for i in range(len(lines)):
            if (lines[i][0].isnumeric() is False) or (lines[i][1:3] != ". "):
                check = False
    if check is True:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH