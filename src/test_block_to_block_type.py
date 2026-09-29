import unittest
from blocktype import BlockType, block_to_block_type
from markdown_to_html_node import *

    


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        matches = block_to_block_type("### This is a heading")
        self.assertEqual(BlockType.HEADING, matches)
        matches = block_to_block_type(f"```\nThis is a code block\nAnother line.\na third line. ```")
        self.assertEqual(BlockType.CODE, matches)
        matches = block_to_block_type(">This is a quote block")
        self.assertEqual(BlockType.QUOTE, matches)
        matches = block_to_block_type(f"- This is a list.\n- Another line.\n- a third line.")
        self.assertEqual(BlockType.UNORDERED_LIST, matches)
        matches = block_to_block_type(f"1. This is a list.\n2. Another line.\n3. a third line.")
        self.assertEqual(BlockType.ORDERED_LIST, matches)
        matches = block_to_block_type("This is normal text.")
        self.assertEqual(BlockType.PARAGRAPH, matches)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )


if __name__ == "__main__":
    unittest.main()